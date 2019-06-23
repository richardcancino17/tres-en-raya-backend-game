from django.conf.urls import url
from .views import *

app_name = 'game'
urlpatterns = [
    url(r'^games/$', ListGamesAPIView.as_view()),
    url(r'^games/(?P<id_game>[^/]+)$', GetGameAPIView.as_view()),
    url(r'^games/(?P<id_game>[^/]+)/moves$', MovesInGameAPIView.as_view()),
]
