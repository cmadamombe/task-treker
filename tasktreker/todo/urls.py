from django.urls import path
from tasktreker.todo import views
# from django.contrib.auth import views as auth_views

app_name = "todo"

urlpatterns = [
    path('create/', views.AddTodoView.as_view(), name='createtodo'),
    path('all/', views.AllTodosList.as_view(), name='alltodo'),
    path('staff/tasks/', views.StaffOnlyTasks.as_view(), name='staff_only_tasks'),
    path('clients/tasks/', views.ClientOnlyTasks.as_view(), name='client_only_tasks'),
    path('In Progress/', views.InProgressTasks.as_view(), name='inprogress_tasks'),
    path('Completed/', views.CompletedTasks.as_view(), name='completed_tasks'),
    path('On Hold/', views.OnHoldTasks.as_view(), name='onhold_tasks'),
    path('Cancelled/', views.CancelledTasks.as_view(), name='cancelled_tasks'),
    path('Personal/', views.PersonalTasks.as_view(), name='personal_tasks'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='update_task'),
    #path('delete/<int:pk>/', views.DeleteTask.as_view(), name='delete_task'),
    path('detail/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('Critical/', views.CriticalTasks.as_view(), name='critical_tasks'),
]
