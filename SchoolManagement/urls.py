from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("School Management System API Running")

urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    path('api/', include('account.urls')),

    path('api/', include('students.urls')),

    path('api/', include('Teacher.urls')),

    path('api/', include('subjects.urls')),

    path('api/', include('attendance.urls')),

    path('api/', include('results.urls')),

    # JWT URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]