from django.shortcuts import render, redirect
from TODO_LIST_APP.models import Task
from TODO_LIST_APP.forms import TaskForm, RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseNotAllowed



def home(request):
    tasks = Task.objects.filter(is_archived=False, is_deleted=False)
    context = {'tasks': tasks, 'form': TaskForm}
    return render(request, 'home.html', context=context)


def archived(request):
    tasks_archived = Task.objects.filter(is_archived=True, is_deleted=False)
    context = {'tasks_archived': tasks_archived}
    return render(request, 'archived.html', context=context)


def deleted(request):
    tasks_deleted = Task.objects.filter(is_archived=False, is_deleted=True)
    context = {'tasks_deleted': tasks_deleted}
    return render(request, 'deleted.html', context=context)


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
    return redirect('home')


def update(request, pk):
    obj = Task.objects.get(pk=pk)
    if request.method == 'POST':
            form = TaskForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
    else:
        action = request.GET.get('action')
        if action == 'is_completed':
            obj.is_completed = not obj.is_completed
        elif action == 'is_archived':
            obj.is_archived = not obj.is_archived
            obj.is_deleted = False 
        elif action == 'is_deleted':
            obj.is_deleted = not obj.is_deleted
            obj.is_archived = False   
        else:
            return redirect('home')
        obj.save()
    return redirect(request.META.get('HTTP_REFERER'))


def empty_recycle_bin(request):
    obj = Task.objects.filter(is_deleted=True)
    obj.delete()
    return redirect('deleted')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
    

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})
