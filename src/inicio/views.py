from django.shortcuts import render

# Create your views here.
def myHomeView(request,*args, **kwargs):
    print(request.user)
    print(args, kwargs)
    myContext = {
        'saludo' : 'hola',
        'lista'  : [1,2,5,4],
    }
    return render(request,"home.html",myContext)