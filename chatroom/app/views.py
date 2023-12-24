from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'app/index.html', {})

# @login_required
def room(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'app/chatroom.html', context)
