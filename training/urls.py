from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name="training_home"),
    path('play/', views.play, name="play"),
    path('play/<video_id>/', views.clip, name="clip"),
    path('knowledge/', views.query, name="knowledge"),
    path('doctor/', views.doctor, name="dr"),
]