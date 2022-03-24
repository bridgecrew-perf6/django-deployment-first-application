from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
def f22(request):
    ss="<center>\
                <h2>Hello good morning user..!!<br /><br />server date and time::"+str(time)+"</h2><hr/>\
        </center>"
    return HttpResponse(ss)