"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import board.views

import reply.views
import user.views
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls), #관리자 페이지
    path('', user.views.mainpage), #메인페이지로 url이 입력되지 않은 상태
    path('ex', user.views.mainindex), #부트스트랩 참조용

    #게시판
    path('board/getdata', board.views.createBoardGet), #게시물 등록
    path('board/readlist', board.views.readlist), #게시물 리스트
    path('board/readdata/<int:bid>', board.views.readdata), # 단일 게시물
    path('board/deleteget/<int:bid>',board.views.deleteget), #게시물 삭제
    path('board/updateget/<int:bid>',board.views.updateget), # 게시물 수정
    #댓글
    path('reply/createreply/<int:bid>', reply.views.createreply), #댓글 등록
    #path('reply/readreplylist', reply.views.readreplylist), #댓글 리스트/ 현재 사용 x
    #path('reply/readreply/<int:bid>', reply.views.readreply), # 단일 댓글 / 현재 사용 x
    path('reply/deletereply/<int:bid>', reply.views.deletereply), # 댓글 삭제
    path('reply/updatereply/<int:bid>', reply.views.updatereply), # 댓글 수정
    #회원가입 실습_자체구현 코드_현재 allauth 사용하므로 사용 x
    #path('user/signup', user.views.signup),
    #path('user/login', user.views.login),
    #path('user/logout', user.views.logout),
    #좋아요 기능
    path('like/<int:bid>',board.views.like),
    #Kakao 로그인 redirect url
    #path('oauth/redirect2',user.views.kakaologin),
    #ALLAUTH
    path('accounts/',include('allauth.urls')), #allauth의 url을 모두 사용
    path('accounts/profile/',user.views.mainpage), #로그인하면 메인페이지로 이동/ 혹 마이페이지로 변경 예정
    #마이페이지
    path('user/mypage', user.views.mypage),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
