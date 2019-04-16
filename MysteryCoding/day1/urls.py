from django.urls import path
from day1 import views
from django.conf.urls import include


urlpatterns = [
    path('email/', views.email, name='email'),
    path('story1/', views.story1, name='story1'),
    path('ip/', views.ip, name='ip'),
    path('riddle/', views.riddle, name='riddle'),
]

