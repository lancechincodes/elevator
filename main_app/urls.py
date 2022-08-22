from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('get-started/', views.GetStarted.as_view(), name="get-started")
]