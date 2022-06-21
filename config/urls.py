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
from django.contrib import admin
from django.urls import path
import board.views
import product.views
import reply.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.views.login), #메인페이지로 url이 입력되지 않은 상태
    #DB연동 실습
    path('product/create', product.views.createFruitGet),
    path('product/createPost', product.views.createFruitPost),
    path('product/getlist', product.views.readFruitGet),
    #게시판 실습
    path('board/getdata', board.views.createBoardGet),
    path('board/readdata', board.views.createReadBoard),
    path('board/readGet/<int:bid>', board.views.readGet),
    path('board/deleteget/<int:bid>',board.views.deleteget),
    path('board/updateget/<int:bid>',board.views.updateget),
    #댓글 실습
    path('reply/createreply', reply.views.createreply),
    path('reply/readreplylist', reply.views.readreplylist),
    path('reply/readreply/<int:bid>', reply.views.readreply),
    path('reply/deletereply/<int:bid>', reply.views.deletereply),
    path('reply/updatereply/<int:bid>', reply.views.updatereply),
    #회원가입 실습
    path('user/signup', user.views.signup),
    path('user/login', user.views.login),
    path('user/logout', user.views.logout),


]
