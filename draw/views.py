from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })  
def composeMusic(request):
    return render(request, 'draw/composeMusic.html', {})
def create(request):
    return render(request, 'draw/create.html', {})
def play(request):
    return render(request, 'draw/play.html', {})
def divhtmlt(request):
    return render(request, 'draw/divhtmlt.html', {})

def divhtmlfour(request):
    return render(request, 'draw/divhtmlfour.html', {})
def lyric(request):
    return render(request, 'draw/lyric.html', {})
def sing(request):
    return render(request, 'draw/sing.html', {})

