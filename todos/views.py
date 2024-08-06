from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')

def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)

    return redirect('todos:index')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')

def login_page(request):
    if request.method== "POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('/login/')
    
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('todos:index')
    
    
    
    return render(request, 'todos/login.html')


def logout_page(request):
    logout(request)
    return redirect('/login')
    
    
    
def register(request):
    if request.method== "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        
        if user.exists():
            
            messages.info(request,'Username already taken')
            return redirect('/register')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        
        messages.info(request,'Account created successfully')
        return redirect('/register')
        
    return render(request, 'todos/register.html')

