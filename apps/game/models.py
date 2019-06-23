from django.db import models
from enum import Enum
from django.contrib.postgres.fields import ArrayField


class Game(models.Model):
    class STATUS(Enum):
        progress = 'progress'
        done = 'done'

    player_1 = models.ForeignKey('account.Player', on_delete=models.CASCADE,
                                 related_name='games')
    player_2 = models.ForeignKey('account.Player', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=[(item.name, item.value)
                                                      for item in STATUS],
                              default='progress')
    board = ArrayField(models.IntegerField(),
                       default=[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
    winner = models.ForeignKey('account.Player', on_delete=models.CASCADE,
                               related_name='games_winner', blank=True,
                               null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return '{} - {} / status : {}'.format(self.player_1, self.player_2,
                                              self.status)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
