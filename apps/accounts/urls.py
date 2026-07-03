from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ChangePasswordView, GetAllUsersView, LogoutView, RegisterView, ProfileView, VerifyEmailView

urlpatterns = [

    # AUTH
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # PROFILE
    path("profile/", ProfileView.as_view(), name="profile"),
    path("users/", GetAllUsersView.as_view(), name="users"),
    path("change-password/", ChangePasswordView.as_view()),
    path("verify-email/<uuid:user_id>/<str:token>/", VerifyEmailView.as_view(),name="verify-email"),

]