from tasktreker.clients.models import Clients
from tasktreker.clients.forms import AddClientForm, ClientUpdateForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.urls import reverse_lazy
# from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
User = get_user_model()


class AddClientView(LoginRequiredMixin, CreateView):
    model = User
    form_class = AddClientForm
    template_name = 'clients/add_new_client.html'
    success_url = reverse_lazy('add_new_client')

    '''def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)'''

    def get_success_url(self):
        return reverse("clients:add_new_client")

    def form_valid(self, form):
        #form.instance.client_created_by = self.request.user
        #form.instance.client_created_by.set([self.request.user])
        messages.add_message(self.request, messages.SUCCESS, "New client details have been successfully added!")
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Clients
    form_class = ClientUpdateForm
    template_name = 'clients/client_update_form.html'
    success_url = reverse_lazy('update_client_details')

    def get_success_url(self):
        return reverse("clients:update_client_details")  # , kwargs={"username": self.request.user.username})

    def get_object(self):
        return Clients.objects.get(user=self.request.user)

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        messages.add_message(self.request, messages.INFO, "The client information have been successfully updated")
        return super().form_valid(form)
