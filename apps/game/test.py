from django.test import TestCase
from apps.account.models import Player
from apps.game.models import Game


class GameTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Player.objects.create(email='prueba_1_test@gmail.com',
                              username='pruebatest1')
        Player.objects.create(email='prueba_2_test@gmail.com',
                              username='pruebatest2')
        Game.objects.create(player_1_id=1, player_2_id=2)

    def test_players_can_play(self):
        game = Game.objects.get(id=1)
        player1 = Player.objects.get(id=1)
        player2 = Player.objects.get(id=2)
        self.assertEqual(player1.play(), 'The player1 play first')
        self.assertEqual(player2.play(), 'The player1 play second')

        # TODO = Finish all the 'assertEquals' in UnitTest
