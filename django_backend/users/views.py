from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

@api_view(['POST'])
def register(request):
    """處理前端送來的會員註冊請求"""
    data = request.data

    # 檢查使用者是否已經存在
    if User.objects.filter(username=data['username']).exists():
        return Response({"error": "帳號已被使用"}, status=status.HTTP_400_BAD_REQUEST)

    # 創建使用者
    user = User.objects.create(
        username=data["username"],
        email=data["email"],
        password=make_password(data["password"]),  # Hash 密碼
    )

    # 產生 JWT Token
    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        },
        status=status.HTTP_201_CREATED,
    )

@api_view(['POST'])
def login(request):
    """處理前端送來的會員登入請求"""
    data = request.data
    user = authenticate(username=data["username"], password=data["password"])

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        )
    else:
        return Response({"error": "帳號或密碼錯誤"}, status=status.HTTP_401_UNAUTHORIZED)