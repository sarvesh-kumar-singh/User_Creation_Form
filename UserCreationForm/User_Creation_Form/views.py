from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm


def Signup(request):
    if request.method =="POST": 
     fm=UserCreationForm(request.POST)
     if fm.is_valid():
      fm.save()

    else:
        fm=UserCreationForm()


    return render (request,'usercreationform/signup.html',{'form':fm})
