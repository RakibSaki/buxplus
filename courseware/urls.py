from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/profile/', views.home)
]