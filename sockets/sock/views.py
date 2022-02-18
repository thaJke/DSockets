from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'sock/index.html')

def room (request, room_name):
    return render(request, 'sock/room.html', {
        'room_name': room_name
    })