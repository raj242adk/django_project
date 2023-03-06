from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title': 'Home New',
        'content':'Happy Holi Guys',
    }
    return render(request,"index.html",data)



def aboutme(request):
    return HttpResponse("Hello this is me MR.Raj");

def Myself(request):
    return HttpResponse("This can be a very good starting of my project i See your progress")


def courseDetails(request,courseid):
    return HttpResponse(courseid)