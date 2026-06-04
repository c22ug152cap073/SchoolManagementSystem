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