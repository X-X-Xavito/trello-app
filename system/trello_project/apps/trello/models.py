from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=40, unique=True)
    email = models.EmailField()
    USERNAME_FIELD = 'name'
    

class BaseModel(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Board(BaseModel):
    users = models.ManyToManyField(MyUser)

    def __str__(self):
        return self.title

class Column(BaseModel):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Card(BaseModel):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    date_created = models.DateField()

    def __str__(self):
        return self.title

class Tag(BaseModel):
    card = models.ManyToManyField(Card)

    def __str__(self):
        return self.title

class Task(BaseModel):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title