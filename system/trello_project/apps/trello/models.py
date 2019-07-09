from django.db import models

class Board(models.Model):
    board_title = models.CharField(max_length=200)

class Card(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    card_title = models.CharField(max_length=200)

class Task(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=200)
    task_completed = models.BooleanField(default=False)