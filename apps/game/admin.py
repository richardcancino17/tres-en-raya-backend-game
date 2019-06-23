from django.contrib import admin
from apps.game.models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_1', 'player_2', 'status', 'board', 'winner')
    search_fields = ('id',)


admin.site.register(Game, GameAdmin)
