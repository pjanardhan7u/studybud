from django.shortcuts import render
from django.http import HttpResponse
from .models import Room



rooms=[
    {'id':1,'name':'lets learn python'},
    {'id':2,'name':'lets learn Java'},
    {'id':3,'name':'lets learn C++'},
]



def home(request):
    rooms=Room.objects.all()
    return render(request,'base/home.html',{'rooms':rooms})


def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'base/room.html',context)
