from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import  TodoForm , UserCreateForm


# Create your views here.

# ----------------------------HOME PAGE-----------------------------
def home(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('boxes')
    
        for id in id_list:
            Task.objects.filter(pk=int(id)).update(done=True)
            return redirect('/')
    try:
        owner = User.objects.get(username=request.user)
        tasks = Task.objects.filter(user=owner, done=False)
        context = {'tasks': tasks}
        return render(request , 'home.html', context)
    except:
        return render(request , 'home.html')

    
# -----------------------------CREATE AN ACCOUNT--------------------------
def create_user(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            return redirect('create_user')

    context = {'form': form}
    return render(request, 'create_user.html', context)


# ----------------------------------LOGIN---------------------------------
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'the user does not exist')

        user = authenticate(request , username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('login')

    return render(request, 'login_page.html')


# ---------LOGOUT---------
def logout_page(request):
    logout(request)
    return redirect('/')


# -------------------ADD A TASK-------------------
@login_required(login_url='login')
def add(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            name = form.save(commit=False)
            name.user = request.user
            name.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'task_form.html', context)


# ------------------EDIT A TASK-------------------
@login_required(login_url='login')
def edit(request, pk):
    task = Task.objects.get(id=pk)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'task_form.html', context)


# ----------------DELETE A TASK---------------------
@login_required(login_url='login')
def delete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'delete.html', context)

# -----------------COMPLETED TASKS------------------
@login_required(login_url='login')
def history(request):
    owner = User.objects.get(username=request.user)
    tasks = Task.objects.filter(user=owner, done=True)
    context = {'tasks': tasks}
    return render(request , 'history.html', context)
   
