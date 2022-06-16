from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def myHomeView(request,*args, **kwargs):
    print(request.user)
    print(args, kwargs)
    myContext = {
        'saludo' : 'hola a todos',
        'lista'  : [1,2,5,4,],
    }
    return render(request,"home.html",myContext)

def myAnotherHomeView(request,*args, **kwargs):
    return HttpResponse('<h1>Esta es otra vista</h1>')