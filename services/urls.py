from django.urls import path
from . import views

# 기본 코드
urlpatterns = [
    path('', views.index),
    path('artii', views.artii),
    path('artii_result', views.artii_result),
    path('push', views.push),
    path('pull', views.pull),
]