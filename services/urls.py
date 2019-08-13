from django.urls import path
from . import views

# 기본 코드
urlpatterns = [
    path('', views.index),
]