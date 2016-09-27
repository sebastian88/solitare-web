from django.db import models


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    codename = models.CharField(max_length=2)
    name = models.CharField(max_length=32)


class InitialPosition(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game)
    shuffled_position = models.IntegerField()
    card = models.ForeignKey(Card)

    class Meta:
        ordering = ('game', 'shuffled_position',)


class Move(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game)
    move_number = models.IntegerField()
    top_card = models.ForeignKey(Card, related_name='card_top_card')
    bottom_card = models.ForeignKey(Card, related_name='card_bottom_card')

    class Meta:
        ordering = ('game', 'move_number',)