from django.urls import path, include
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.dtr, name='dtr'),
    path('addtime/', views.addTime, name="addtime"),
    path('login/', views.loginpage, name="loginpage"),
    path('register/', views.registerpage, name="registerpage"),
    path('loginproc/', views.loginproc, name='loginproc'),
    path('logout/', views.logoutview, name='logout'),
    path('registerproc/', views.registerproc, name='registerproc')
]
