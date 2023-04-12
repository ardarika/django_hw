"""
URL configuration for django_hw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myapp.views import blogs, about, comment, create, delete, update, register, login, profile, change_password, more


urlpatterns = [
    path('blogs/', blogs),
    path('about/', about),
    path('', blogs),
    path('<slug:slug>/', more),
    path('<slug:slug>/comment/', comment),
    path('create/', create),
    path('<slug:slug>/update/', update),
    path('<slug:slug>/delete/', delete),
    path('profile/<str:username>/', profile),
    path('change_password/', change_password),
    path('register/', register),
    path('login/', login),
    path('logout/', blogs),
]