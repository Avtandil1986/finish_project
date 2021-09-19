import datetime
import random
import secrets

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
#
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OTPCode


class OTPView(APIView):
    def post(self, request):
        phone = request.data["phone"]
        try:
            user = User.objects.get(username=phone)
        except:
            user = User.objects.create_user(
                username=phone,
                password=str(secrets.token_bytes(20)),
                email="avto@a.ru",
                is_active=False
            )
        OTPCode.objects.create(
            user=user,
            code=str(random.randint(100, 100000)),
            valid_until=datetime.datetime.now() + datetime.timedelta(minutes=5)
        )
        return Response(data={"massage": "Code created"})


class OTPConfirmView(APIView):
    def post(self, request):
        code = request.data["code"]
        print(code)
        otp_list = OTPCode.objects.filter(
            code=code,
            valid_until__gte=datetime.datetime.now()

        )
        print(otp_list)
        if otp_list.count() > 0:
            try:
                token = Token.objects.get(user=otp_list[0].user)

            except Token.DoesNotExist:
                token = Token.objects.create(user=otp_list[0].user)

            return Response(data={"key": token.key})
        else:
            return Response(data={"message": "Invalid code"})
