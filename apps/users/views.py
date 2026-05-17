from datetime import datetime

from django.contrib.auth import authenticate
from django.template.context_processors import request
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.serializers import UserLoginSerializer
from apps.users.serializers.user import RegisterUserSerializer
from apps.users.utils import set_jwt_cookies, REFRESH_COOKIE_NAME, clear_jwt_cookies, set_refresh_cookie, \
    set_access_cookie


# class UserProfileView(APIView):
#     permission_classes = (AllowAny,)
#     def get(self, request, format=None):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
#


class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        data = request.data

        serializer = UserLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        try:
            response = Response(
                status=status.HTTP_200_OK,
            )

            set_jwt_cookies(response=response, user=user)

            # 6. вернуть ответ
            return response

        except Exception as e:
            # 6. вернуть ответ
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    "message": str(e)
                }
            )



class LogoutUser(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            refresh_token = request.COOKIES.get(REFRESH_COOKIE_NAME)
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

        except TokenError:
            pass

        except Exception as e:
            print("logout >>>", e)
            return Response(
                data={
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        response = Response(
            status=status.HTTP_200_OK,
        )

        clear_jwt_cookies(response=response)

        return response


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response = Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

        set_jwt_cookies(response=response, user=user)

        return response

class RefreshUserTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        refresh_token = request.COOKIES.get(REFRESH_COOKIE_NAME)

        if not refresh_token:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            response = Response(status=status.HTTP_200_OK)
            set_access_cookie(response=response, access_token=access_token)

            return response

        except TokenError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)








