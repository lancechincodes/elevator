from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('applications/', views.ApplicationList.as_view(), name="applications_index"),
    path('applications/<int:pk>/', views.ApplicationDetail.as_view(), name="applications_detail"),
    path('applications/create/', views.ApplicationCreate.as_view(), name="application_create"),
    path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name="applications_update"),
    path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name="applications_delete"),
]