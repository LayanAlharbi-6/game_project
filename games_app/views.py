from django.shortcuts import render ,get_object_or_404
from .models import Game,Developer
# Create your views here.
def home(request):
    return render (request,'home.html')


def game_list(request):
  games=Game.objects.all()
       return render (request,'game.list'{'games':games})


def game_detaliss(request ,game_id):
    game=get_object_or_404(Game,id=game_id)
     return render (request,'game.detaliss'{'game':game})
 
def add_games(request):
developer1=Developer.objects.Create(name="ali")
developer2=Developer.objects.Create(name="yazeed")

Game.objects.Create(title="HS",developer=developer1)
Game.objects.Create(title="MA",developer=developer2)