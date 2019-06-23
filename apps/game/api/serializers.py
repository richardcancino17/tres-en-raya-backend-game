from apps.game.models import Game
from apps.account.api.serializers import ListPlayersSerializer
from apps.account.models import Player
from rest_framework import serializers


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

    def get_winner(self, game):
        bo = []
        le = []
        return ((bo[6] == le and bo[7] == le and bo[
            8] == le) or  # across the top
                (bo[3] == le and bo[4] == le and bo[
                    5] == le) or  # across the middle
                (bo[0] == le and bo[1] == le and bo[
                    2] == le) or  # across the bottom
                (bo[6] == le and bo[3] == le and bo[
                    0] == le) or  # down the left side
                (bo[7] == le and bo[4] == le and bo[
                    1] == le) or  # down the middle
                (bo[8] == le and bo[5] == le and bo[
                    2] == le) or  # down the right side
                (bo[6] == le and bo[4] == le and bo[2] == le) or  # diagonal
                (bo[8] == le and bo[4] == le and bo[0] == le))  # diagonal


class GetGameSerializer(serializers.ModelSerializer):
    player_1 = serializers.StringRelatedField(read_only=True)
    player_2 = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Game
        fields = ('__all__')


class MovesInGameSerializer(serializers.Serializer):
    def validate_number(value):
        print(value)
        if value < 0 or value > 8:
            raise serializers.ValidationError({'details': [{
                'object': 'Error',
                'message': 'Incorrect position',
                'code': 'G00-002'
            }]})

    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(),
                                                required=True)
    position = serializers.IntegerField(validators=[validate_number],
                                        required=True)

