from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em> My Second Page!</em>")

def help(request):
    helpdict = {'help_insert' : 'HELP PAGE'}
    return render(request, 'App2/help.html', context=helpdict)
