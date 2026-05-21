from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.

def sign_up(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'users/sign_up.html', {'form':form})
    else:
        form=SignUpForm()
        return render(request, 'users/sign_up.html', {'form':form})
    
    