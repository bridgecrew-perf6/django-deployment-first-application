from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f11(request):
    ss="<center>\
                <h2>Hello good morning user..!! have a nice day..</h2><hr/>\
                <h3>whishes from APP1</h3><hr/>\
        </center>"
    return HttpResponse(ss)