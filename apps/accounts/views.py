from rest_framework.views import APIView
from rest_framework import generics
from .serializers import RegisterSerializer, UserSerializer
from .models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .tokens import email_verification_token


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return self.request.user

class GetAllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"})
        except Exception:
            return Response({"error": "Invalid token"}, status=400)
        
class ChangePasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.user
        old = request.data.get("old_password")
        new = request.data.get("new_password")

        if not user.check_password(old):
            return Response({"error": "Wrong password"}, status=400)

        user.set_password(new)
        user.save()

        return Response({"message": "Password updated"})
    
class VerifyEmailView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, user_id, token):

        try:
            user = User.objects.get(id=user_id)

            if email_verification_token.check_token(user, token):

                user.is_active = True
                user.is_verified = True
                user.save()

                return Response({
                    "message": "Email verified successfully. Account activated."
                })

            return Response({
                "error": "Invalid or expired token"
            }, status=400)

        except User.DoesNotExist:
            return Response({
                "error": "User not found"
            }, status=404)