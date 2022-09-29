from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from .models import tododata
from . import forms
# Create your views here.

def index(request):
    
    if request.method=="POST":
        todo = request.POST.get('todo')
        requested_data = tododata(
            todo = todo,
            is_finished=False,
        )
        requested_data.save()

    alldata = tododata.objects.all()
    
    #フォームを表示する設定
    #forms.pyからtodo_formsクラスをインスタンス化し、dictに格納
    form = forms.todo_form(request.GET or None)
    dict = {
        "form": form,#入力フォームの情報をhtmlに渡す
        "app": "TodoList",
        "alldata": alldata,
    }
    return render(request, "index.html", dict)

def get(request):
    if request.headers.get("Content-Type") == 'application/json':
        alldata = tododata.objects.values()
        #print(alldata)
        todos = list(alldata)
        #print(todos)
        return JsonResponse(todos, safe=False, status=200)
    return render(request, "index.html")

def createNewTodo(request):
    requested_data = json.loads(request.body)
    #print(whatTodo, type(whatTodo))
    new_data = tododata(
            todo = requested_data["whatTodo"],
            is_finished=False,
    )
    new_data.save()
    return JsonResponse({"whatTodo": model_to_dict(new_data)}, status=200)

def update_finishedFlag(request):
    #
    if request.method=="POST":
        requested_data = json.loads(request.body)
        
        todo = requested_data["todo"]
        finised_flag = requested_data["is_finished"]
        id = requested_data["id"]
        if finised_flag==False:
            finised_flag = True
        else:
            finised_flag = False
        
        chosen_row = tododata.objects.get(id=id)
        chosen_row.is_finished = finised_flag
        chosen_row.save()

        alldata = tododata.objects.values()
        todos = list(alldata)
        return JsonResponse(todos, safe=False, status=200)


def deleteTodo(request):
    if request.method=="POST":
        requested_data = json.loads(request.body)
        print(requested_data)
        id = requested_data["id"]

        tododata.objects.filter(id=id).delete()
        alldata = tododata.objects.values()
        todos = list(alldata)
        return JsonResponse(todos, safe=False, status=200)

