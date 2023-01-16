from django.urls import path

from . import views


app_name= 'cep'

urlpatterns = [
    path('', views.getAndPostData, name="home"),
    path('result/', views.resultView, name="result"),
]
