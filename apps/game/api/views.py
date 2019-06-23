from django.shortcuts import render
from rest_framework import generics, status, filters
from apps.game.models import Game
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from apps.game.api.serializers import ListGamesSerializer, GetGameSerializer, \
    MovesInGameSerializer
from apps.game.functions import see_status_game
from rest_framework.generics import get_object_or_404


class ListGamesAPIView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = ListGamesSerializer
    permission_classes = IsAuthenticated,


class GetGameAPIView(generics.RetrieveAPIView):
    serializer_class = GetGameSerializer
    permission_classes = IsAuthenticated,

    def get_object(self):
        id = self.kwargs.get('id_game')
        try:
            return Game.objects.get(id=id)
        except Game.DoesNotExist:
            return None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            serializer = GetGameSerializer(instance, context={
                'request': request})
            return Response(serializer.data)
        else:
            return Response({'details': [{
                'object': 'Error',
                'message': 'Game does not exist!',
                'code': 'G00-001'
            }]}, status=status.HTTP_404_NOT_FOUND)


class MovesInGameAPIView(generics.GenericAPIView):
    serializer_class = MovesInGameSerializer
    permission_classes = IsAuthenticated,

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={"request": request})
        serializer.is_valid(raise_exception=True)
        id = self.kwargs.get('id_game')
        game = get_object_or_404(Game.objects.all(), id=id)
        position = serializer.validated_data.get('position')
        player = serializer.validated_data.get('player')
        status_game = see_status_game(game)

        if status_game:
            return Response({'details': [{
                'object': 'Successful',
                'message': 'The game have finished, please, check it out '
                           'the details',
                'code': 'G00-005'
            }]}, status=status.HTTP_200_OK)

        if game.board[position] == -1:
            game.board[position] = player.id
            game.save()
            return Response({'details': [{
                'object': 'Successful',
                'message': 'Move done in position in {}'.format(position),
                'code': 'G00-003'
            }]}, status=status.HTTP_200_OK)
        else:
            return Response({'details': [{
                'object': 'Error',
                'message': 'The position {} have been used'.format(position),
                'code': 'G00-004'
            }]}, status=status.HTTP_404_NOT_FOUND)
