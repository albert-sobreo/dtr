from django.urls import path, include
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.dtr, name='dtr'),
    path('addtime/', views.addTime, name="addtime")
]
