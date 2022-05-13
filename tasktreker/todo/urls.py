from django.urls import path
from tasktreker.todo import views
# from django.contrib.auth import views as auth_views

app_name = "todo"

urlpatterns = [
    path('create', views.AddTodoView.as_view(), name='createtodo'),
    path('all', views.AllTodosList.as_view(), name='alltodo'),
]
