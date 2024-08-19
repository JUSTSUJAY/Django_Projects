from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('-date')
    if request.method == "POST":
        form_received = TodoForm(request.POST)
        if form_received.is_valid():
            form_received.save()
            return redirect("index")
    form = TodoForm()
    page = {
        "forms": form,
        "list": todo_list,
        "title": "TODO LIST",
        }
    return render(request, "index.html",page)  

def delete(request, pk):
    retrieved_todo = Todo.objects.get(id=pk)
    retrieved_todo.delete()
    messages.info(request, "Todo deleted successfully")
    return redirect("index")