from django.urls import path

from . import views

app_name = 'trello'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_board', views.create_board, name='create_board')



]