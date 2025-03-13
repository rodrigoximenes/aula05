from django.shortcuts import render
from .models import Todo


def todo_list(request):
    todos_lista  = Todo.objects.all() 
    return render(request, "todos/todo_list.html", {"todos": todos_lista});