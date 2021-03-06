from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #route, view, name
    # empty '' means its the root, views is a file in this folder. index is the class or fun or ~
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    
]
