from django.http import HttpResponse
from django.shortcuts import render

from .models import Board

# Create your views here.

def index(request):
    template = 'trello/index.html'
    boards_list = Board.objects.all()

    context = {
        'boards_list': boards_list
    }
    return render(request,  template, context)

def create_board(request):
    template = 'trello/create_board.html'
    return render(request, template)