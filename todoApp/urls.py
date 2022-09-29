from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get", views.get, name="get"),
    path("create", views.createNewTodo, name="create"),
    path("update", views.update_finishedFlag, name="update"),
    path("delete", views.deleteTodo, name="delete"),
]