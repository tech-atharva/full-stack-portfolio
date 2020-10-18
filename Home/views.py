from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "Home/index.html")


def About(request):
    return HttpResponse("hello wolrd About")


def Services(request):
    return HttpResponse("hello wolrd Services")


def Contact(request):
    return HttpResponse("hello wolrd Contact")
