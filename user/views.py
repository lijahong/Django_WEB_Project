from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
import requests
from user.models import User

""" #allauth 안쓰고 자체 구현 코드_현재 사용x
def signup(request): #회원가입
    if request.method == "GET":
        signupForm = UserCreationForm() #Django에 저장된 form
        return render(request,'user/signup.html',{'signupForm':signupForm})
    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST) #username, password1, password2 반환해야한다
        if signupForm.is_valid(): #값이 유효해야 회원가입이 가능하다, 조건은 불러온 Django form에 저장되있다
            user = signupForm.save(commit=False)
            user.save()
            return redirect('/main')
        return redirect('/main')

def login(request): #로그인
    if request.method == "GET":
        loginForm = AuthenticationForm() #login용 form
        return render(request,"user/login.html",{"loginForm":loginForm})
    elif request.method == "POST": #원래는 DB에서 DATA를 불러와 비교하겠지만, Django는 그 기능이 구현되어있다
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user()) #loginform에서 user만 가져옴, 이 코드 안에는 사용자 이름을 가지고 그 이름에 해당하는 passwor를 DB로 부터 가져와 비교하는 기능이 구현되어있다. 따라서 FORM에서 유저정보를 불러와 전달해줘야한다
            return redirect("/main")
        else:
            return redirect("/user/login")


def logout(request):
    auth_logout(request)
    return redirect("/main")
"""
def mainpage(request):
    return render(request, 'mainpage.html')

def mainindex(request):
    return render(request,'index.html')
"""
def kakaologin(request): #kakao 로그인 용
    code = request.GET.get('code')
    data = {'grant_type': 'authorization_code',
            'client_id':'2c37b1f9400581ab999ecbc87ebc0ea2', #발급받은 앱 키
            'redirect_uri': 'http://127.0.0.1:8000/oauth/redirect2', #redirect url
            'code':code #받은 인가 코드
            }
    headers = {'Contents-type':'application/x-www-form-urlencoded;charset=utf-8'}
    res = requests.post('https://kauth.kakao.com/oauth/token', data=data, headers=headers) #import request해야한다, request package 설치 필요, res는 응답 받은 객체 이다
    token_json = res.json() #json 파일로 받아온다
    access_token = token_json['access_token'] #access_token 받아오기


    #token 전송하여 정보 가져오기
    headers = {'Authorization': 'Bearer '+access_token,
               'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
    res = requests.get('https://kapi.kakao.com//v2/user/me', headers=headers)
    #가져온 정보에서 필요한 정보 따오기
    profile_res = res.json()
    print(profile_res)
    nickname = profile_res['kakao_account']['profile']['nickname'] #kakao에서 받아온 이름
    kakaoid = profile_res['id'] #kakao id

    #django의 user를 가져오기
    user = User.objects.filter(email=kakaoid)
    if user.first() is not None: #로그인
        auth_login(request, user.first(), backend='django.contrib.auth.backends.ModelBackend')
        return redirect("/main")
    else: #회원가입
        user = User()
        user.email = kakaoid  # email란에 kakaoid를 넣어주겠다. email양식이 아니어도 가능하다
        user.username = nickname
        user.save()
        print('save it--------------------------')
        return redirect('/main')
    return redirect("/user/login")
"""