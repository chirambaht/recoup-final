from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Practice
from .forms import AtheleteRegisterForm, PracticeRegisterForm, UserUpdateForm, AtheleteUpdateForm

# Create your views here.
def home(request):
    context = {'title':'Home'}
    pracs = Practice.objects.all()[:3]
    context['practices'] = pracs
    return render(request, 'dashboard/homepage.html', context)

def about(request):
    context = {'title':'About'}
    return render(request, 'dashboard/about.html', context)

def login(request):
    context = {'title':'Login'}
    return render(request, 'dashboard/login.html', context)

def register(request):

    if request.method == 'POST':
        form = AtheleteRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = AtheleteRegisterForm()
    return render(request, 'dashboard/register.html', {'form': form, 'title':'Register Athelete'})

def registerPractice(request):

    if request.method == 'POST':
        form = PracticeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Practice created {name}!')
            return redirect('loginPractice')
    else:
        form = PracticeRegisterForm()
    return render(request, 'dashboard/practice-register.html', {'form': form, 'title':'Register Practice'})
