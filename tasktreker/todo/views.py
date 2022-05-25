from .forms import AddTodoForm, UpdateTodoForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from .models import Todo
from django.contrib import messages
from django.views import View
from .filters import TaskFilter

User = get_user_model()


# we only create a TaskBaseView so that we don’t repeat the model, fields and success_url info lines, then we make our
# Task View Classes inherit from both TaskBaseView and the respective Generic View Classes that Django already has for
# doing CRUD operations.
class TaskBaseView(View):
    model = Todo
    success_url = reverse_lazy('todo:alltodo')
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = TaskFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context


class AddTodoView(LoginRequiredMixin, TaskBaseView, CreateView):
    form_class = AddTodoForm
    template_name = 'todo/createtodo.html'
    success_url = reverse_lazy('todo:createtodo')

    try:
        def form_valid(self, form):
            form.instance.created_by = self.request.user
            messages.add_message(self.request, messages.SUCCESS, 'New Task has been successfully saved into the database')
            return super().form_valid(form)
    except:
        pass


class UpdateTask(LoginRequiredMixin, TaskBaseView, UpdateView):
    form_class = UpdateTodoForm
    template_name = 'todo/update_task.html'

    try:
        def form_valid(self, form):
            messages.add_message(self.request, messages.SUCCESS, 'The task has been successfully updated')
            return super().form_valid(form)
    except:
        pass


# class DeleteTask(LoginRequiredMixin, DeleteView):
    # template_name = 'todo/delete_task.html'


class TaskDetail(LoginRequiredMixin, DetailView):
    template_name = 'todo/taskdetails.html'

    def get_queryset(self):
        return Todo.objects.all()


# view to list all tasks
class AllTodosList(LoginRequiredMixin, TaskBaseView, ListView):
    # You can avoid using the template_name attribute.
    # Because ListView’s default behavior is to utilize a template called / _list.html.
    template_name = 'todo/list_all_todos.html'
    # You can also avoid using context_object_name.
    # Since ListView’s default behavior is to fill the template with the context name object_list.
    # supply a get_queryset() implementation if you want to filter the queryset differently for different web requests.
    # queryset = Todo.objects.all()
    # paginate_by = 3
    # method to filter queries by logged in user.
    # def get_queryset(self):
    # return Todo.objects.filter(todoowner = self.request.user)

    def get_queryset(self):
        queryset = Todo.objects.all()
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


# view to list tasks in the database assigned to task owner/client
class ClientOnlyTasks(LoginRequiredMixin, TaskBaseView, ListView):
    template_name = 'todo/client_only_tasks.html'

    def get_queryset(self):
        queryset = Todo.objects.filter(client__user=self.request.user)
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


# view to list tasks in the database assigned to staff
class StaffOnlyTasks(LoginRequiredMixin, TaskBaseView, ListView):
    template_name = 'todo/staff_only_tasks.html'

    def get_queryset(self):
        queryset = Todo.objects.filter(assigned__user=self.request.user)
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


# view to list tasks in the database that are completed
class CompletedTasks(LoginRequiredMixin, TaskBaseView, ListView):
    template_name = 'todo/completed_tasks.html'

    def get_queryset(self):
        queryset = Todo.objects.filter(status='Completed')
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


# view to list tasks in the database that are in progress
class InProgressTasks(LoginRequiredMixin, TaskBaseView, ListView):
    template_name = 'todo/inprogress_tasks.html'

    def get_queryset(self):
        queryset = Todo.objects.filter(status='In Progress')
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


# view to list tasks in the database that are on hold
class OnHoldTasks(LoginRequiredMixin, TaskBaseView, ListView):
    template_name = 'todo/onhold_tasks.html'

    def get_queryset(self):
        queryset = Todo.objects.filter(status='On Hold')
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


# view to list tasks in the database that are cancelled
class CancelledTasks(LoginRequiredMixin, TaskBaseView, ListView):
    template_name = 'todo/cancelled_tasks.html'

    def get_queryset(self):
        queryset = Todo.objects.filter(status='Cancelled')
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


# Added new views - 17 May 2022 - Chuck
# view to list tasks in the database that are cancelled
class PersonalTasks(LoginRequiredMixin, TaskBaseView, ListView):
    template_name = 'todo/personal_tasks.html'

    def get_queryset(self):
        queryset = Todo.objects.filter(type='Personal')
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


class CriticalTasks(LoginRequiredMixin, TaskBaseView, ListView):
    template_name = 'todo/critical_tasks.html'

    def get_queryset(self):
        queryset = Todo.objects.filter(priority='Critical', status='In Progress')
        filter = TaskFilter(self.request.GET, queryset)
        return filter.qs


