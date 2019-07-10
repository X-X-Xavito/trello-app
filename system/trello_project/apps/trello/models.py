from django.db import models

class Board(models.Model):
    board_title = models.CharField(max_length=200)

    def __str__(self):
        return self.board_title

class Card(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    card_title = models.CharField(max_length=200)

    def __str__(self):
        return self.card_title


class Task(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=200)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_description
