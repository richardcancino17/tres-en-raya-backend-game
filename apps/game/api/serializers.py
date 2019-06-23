from apps.game.models import Game
from apps.account.models import Player
from rest_framework import serializers


class CreateGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('player_2',)


class ListGamesSerializer(serializers.ModelSerializer):
    players = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ('status', 'id', 'created_at', 'players')

    def get_players(self, game):
        players = []
        players.append({'id': game.player_1.id})
        players.append({'id': game.player_2.id})
        return players


class GetGameSerializer(serializers.ModelSerializer):
    player_1 = serializers.StringRelatedField(read_only=True)
    player_2 = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Game
        fields = ('__all__')


class MovesInGameSerializer(serializers.Serializer):
    def validate_number(value):
        if value < 0 or value > 8:
            raise serializers.ValidationError({
                'object': 'Error',
                'message': 'Incorrect position',
                'code': 'G00-002'
            })

    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(),
                                                required=True)
    position = serializers.IntegerField(validators=[validate_number],
                                        required=True)
