from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    ss="<h2>hello user,welcome to django FirstProject and FirstApp<h2><h3>hi sai how are u..<h3>"
    return HttpResponse(ss)
    
def show(request):
    ss= "<center>\
            <h1>welcome to DJANGO HTML webpage</h1>\
            <hr / width=500 color=blue size=10>\
            <h2>welcome to DJANGO HTML webpage</h2>\
            <hr / width=450 color=red size=8>\
            <h3>welcome to DJANGO HTML webpage</h3>\
            <hr / width=400 color=green size=6>\
            <h4>welcome to DJANGO HTML webpage</h4>\
            <hr / width=350 color=orange size=4>\
            <h5>welcome to DJANGO HTML webpage</h5>\
            <hr / width=300 color=yellow size=2>\
            <h6>welcome to DJANGO HTML webpage</h6>\
            <hr / width=250 color=pink size=0>\
            </center>";
    return HttpResponse(ss)    