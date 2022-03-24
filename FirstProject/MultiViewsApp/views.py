from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#this views is  going to response for MultiViewsApps
def f1(request):
    return HttpResponse("<h2>godd morning user..!! have a nice day..</h2><hr/>")
def f2(request):
    return HttpResponse("<h2>godd afetrnoon user..!! hope ur doing good..</h2><hr/>")
def f3(request):
    return HttpResponse("<h2>godd evening user..!! how was ur day..?</h2><hr/>")
    
