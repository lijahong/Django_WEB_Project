from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

def signup(request): #회원가입
    if request.method == "GET":
        signupForm = UserCreationForm() #Django에 저장된 form
        return render(request,'user/signup.html',{'signupForm':signupForm})
    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid(): #값이 유효해야 회원가입이 가능하다, 조건은 불러온 Django form에 저장되있다
            user = signupForm.save(commit=False)
            user.save()
        return redirect('/board/readdata')

def login(request): #로그인
    if request.method == "GET":
        loginForm = AuthenticationForm() #login용 form
        return render(request,"user/login.html",{"loginForm":loginForm})
    elif request.method == "POST": #원래는 DB에서 DATA를 불러와 비교하겠지만, Django는 그 기능이 구현되어있다
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user()) #loginform에서 user만 가져옴, 이 코드 안에는 사용자 이름을 가지고 그 이름에 해당하는 passwor를 DB로 부터 가져와 비교하는 기능이 구현되어있다. 따라서 FORM에서 유저정보를 불러와 전달해줘야한다
            return redirect("/board/readdata")

