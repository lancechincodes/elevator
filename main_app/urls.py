from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('applications/', views.applications_index, name="applications_index"),
    path('applications/incomplete', views.applications_ic, name="applications_ic"),
    path('applications/applied', views.applications_a, name="applications_a"),
    path('applications/interviews', views.applications_i, name="applications_i"),
    path('applications/offers', views.applications_o, name="applications_o"),
    path('applications/rejected', views.applications_r, name="applications_r"),
    path('applications/create/', views.ApplicationCreate.as_view(), name="applications_create"),
    path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name="applications_update"),
    path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name="applications_delete"),
    path('accounts/signup/', views.signup, name='signup'),
]

