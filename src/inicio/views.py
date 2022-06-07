from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return render(request,"home.html",{})