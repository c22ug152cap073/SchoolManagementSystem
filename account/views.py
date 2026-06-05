from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class LoginAPIView(APIView):

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(
            username=email,
            password=password
        )

        if user is not None:
            return Response({
                "status": True,
                "message": "Login Successful",
                "email": user.email
            })

        return Response({
            "status": False,
            "message": "Invalid Credentials"
        }, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Welcome",
            "email": request.user.email
        })

from students.models import Student
from Teacher.models import Teacher
from subjects.models import Subject
from attendance.models import Attendance
from results.models import Result   

class DashboardAPIView(APIView):

    def get(self, request):

        data = {
            "total_students": Student.objects.count(),
            "total_teachers": Teacher.objects.count(),
            "total_subjects": Subject.objects.count(),
            "total_attendance": Attendance.objects.count(),
            "total_results": Result.objects.count(),
        }

        return Response(data)