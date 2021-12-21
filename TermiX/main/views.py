from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"main/home.html",{})


def ErrorPage(request,error):
    return render(request,"main/error.html",{'error':error})
