from django.contrib.auth import authenticate, login
from requests.exceptions import HTTPError
from rest_framework.authtoken.models import Token
from apps.account.models import Player
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.message import EmailMessage
from requests.exceptions import HTTPError
from django.template import loader
from django.conf import settings
from rest_framework import serializers
from social.exceptions import AuthCanceled


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('email', 'password', 'username',)
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = Player.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        error_messages={"blank": "Este campo es obligatorio"})
    password = serializers.CharField(
        error_messages={"blank": "Este campo es obligatorio"})

    def validate(self, attrs):
        self.user_cache = authenticate(email=attrs["email"],
                                       password=attrs["password"])
        if not self.user_cache:
            raise serializers.ValidationError("Invalid login")
        else:
            return attrs

    def get_user(self):
        return self.user_cache


class FacebookLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField(
        error_messages={"blank": "Este campo es obligatorio"})

    def validate(self, attrs):
        request = self.context.get("request")
        self.user_cache = None
        try:
            self.user_cache = request.backend.do_auth(attrs.get("access_token"))
            return attrs
        except HTTPError:
            raise serializers.ValidationError("Invalid facebook token")

    def get_user(self):
        return self.user_cache


class ListPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'username',)
