from django.urls import path
from .views import LoginAPIView, ProfileAPIView, DashboardAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard'),
]