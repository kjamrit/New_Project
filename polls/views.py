from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Polls Home </h1>')
    
def greeting(request):
    return HttpResponse('<h1> How you doin? </h1>')

def about(request):
    return HttpResponse('<h1> Polls About </h1>')