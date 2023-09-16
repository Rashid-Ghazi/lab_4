from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("I ,Waseem and Ali in current class ")


def ali_hassan(request):
    #return HttpResponse('this is ali hassam house')
    return render(request, "students/ali.html", {})


def waseem(request):
    #return HttpResponse('this is waseem house')
    return render(request, "students/waseem.html", {})

def rashid(request):
    #return HttpResponse('this is sir rashid house')
    return render(request, "students/sir_rashid.html", {}) 


# Create your views here.
