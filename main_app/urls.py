from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('applications/', views.applications_index, name="applications_index"),
    path('applications/create/', views.ApplicationCreate.as_view(), name="applications_create"),
    path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name="applications_update"),
    path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name="applications_delete"),
    path('accounts/signup/', views.signup, name='signup')
]

