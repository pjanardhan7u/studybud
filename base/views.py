from django.shortcuts import render
from django.http import HttpResponse


rooms=[
    {'id':1,'name':'lets learn python'},
    {'id':2,'name':'lets learn Java'},
    {'id':3,'name':'lets learn C++'},
]



def home(request):
    return render(request,'home.html',{'rooms':rooms})


def room(request):
    return render(request,'room.html')
