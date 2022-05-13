from django.shortcuts import redirect
from .forms import AddTodoForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from .models import Todo
from django.contrib import messages
User = get_user_model()

# Create your views here.
class AddTodoView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = AddTodoForm
    template_name = 'todo/createtodo.html'
    success_url = reverse_lazy('alltodo')

    def get_success_url(self):
        return reverse('todo:alltodo')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'New Task has been successfully saved into the database')
        return super().form_valid(form)

# 10 May 2022 - added the view to list all todos
class AllTodosList(LoginRequiredMixin, ListView):
    model = Todo
    # You can avoid using the template_name attribute. Because ListView’s default behavior is to utilize a template called / _list.html.
    template_name = 'todo/list_all_todos.html'
    # You can also avoid using context_object_name. Since ListView’s default behavior is to fill the template with the context name object_list.
    context_object_name = 'tasks'
    # supply a get_queryset() implementation if you want to filter the queryset differently for different web requests.
    # queryset = Todo.objects.filter(status = 'Completed')
    # paginate_by = 3

    # method to filter queries by logged in user.
    #def get_queryset(self):
        #return Todo.objects.filter(todoowner = self.request.user)

    def get_queryset(self):
        return Todo.objects.all()
