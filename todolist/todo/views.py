from django.shortcuts import redirect, render
from .models import todoData
from datetime import datetime

# Create your views here.

def todo(request):
    if(request.method=='POST'):
        title=request.POST['title']
        nowi=datetime.now()
        dt_string = nowi.strftime("%H:%M:%S")
        created=nowi
        completed=False
        todoData.objects.create(title=title,creation=created,status=completed)
    queryset=todoData.objects.order_by("creation")
    return render(request,"todo/todo.html",{"tasks":queryset})
def delete(request,id):
    toDelete=todoData.objects.get(id=id)
    toDelete.delete()
    return redirect("todo")
def complete(request,id):
    toComplete=todoData.objects.get(id=id)
    toComplete.status=True
    toComplete.save()
    return redirect("todo")