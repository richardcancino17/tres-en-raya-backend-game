from django.shortcuts import render
from rest_framework import generics, status, filters
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated, AllowAny
from social.apps.django_app.utils import psa
from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = AllowAny,

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={"request": request})
        serializer.is_valid(raise_exception=True)
        token, created = Token.objects.get_or_create(user=serializer.get_user())
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class MobileLoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={"request": request})
        serializer.is_valid(raise_exception=True)
        token, created = Token.objects.get_or_create(user=serializer.get_user())
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class FacebookMobileLoginAPI(MobileLoginAPI):
    '''Facebook Login'''
    serializer_class = FacebookLoginSerializer
    permission_classes = AllowAny,

    @method_decorator(psa('player:facebook-mobile-login'))
    def dispatch(self, request, *args, **kwargs):
        return super(FacebookMobileLoginAPI, self).dispatch(request, *args,
                                                            **kwargs)


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = AllowAny,

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class ListPlayersAPIView(generics.ListAPIView):
    serializer_class = ListPlayersSerializer
    queryset = Player.objects.all()
    permission_classes = [AllowAny, ]
