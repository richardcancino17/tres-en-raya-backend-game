from django.test import TestCase
from apps.account.models import Player
from apps.game.models import Game


class GameTestCase(TestCase):
    def setUp(self):
        Player.objects.create(email='prueba_1_test@gmail.com',
                              username='pruebatest1')
        Player.objects.create(email='prueba_2_test@gmail.com',
                              username='pruebatest2')
        Game.objects.create(player_1_id=1, player_2_id=2)

    def test_players_can_play(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        game = Game.objects.get(id=1)
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
