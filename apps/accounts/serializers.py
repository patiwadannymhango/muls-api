from rest_framework import serializers
from .tokens import email_verification_token
from .utils import send_verification_email
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "role"]

    def create(self, validated_data):
        request = self.context.get("request")

        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )

        # ❗ disable login until verified
        user.is_active = False
        user.save()

        # generate token
        token = email_verification_token.make_token(user)

        # build verification link
        verification_link = f"http://127.0.0.1:8000/api/v1/auth/verify-email/{user.id}/{token}/"

        # send email
        # send_verification_email(user, token, verification_link)
        send_verification_email(user, verification_link)

        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "role", "phone_number"]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()