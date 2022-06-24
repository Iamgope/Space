from django.shortcuts import render,redirect
from .form import SignUpForm
from django.contrib.auth import login
# Create your views here.
def frontPage(request):
    return render(request,'core/homepage.html')

def SignUp(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            print(user)
            login(request,user)
            return redirect('frontPage')
    else:
        form=SignUpForm()
    return render(request,'core/signUp.html',{'form':form}) 