from django.conf.urls import url
from .views import *

app_name = 'player'
urlpatterns = [
    url(r'^player/register$', CreateUserAPIView.as_view()),
    url(r'^player/login/mobile/(?P<backend>[^/]+)$',
        FacebookMobileLoginAPI.as_view(), name="facebook-mobile-login"),
    url(r'^player/login$', LoginAPIView.as_view()),
    url(r'^players$', ListPlayersAPIView.as_view()),
]
