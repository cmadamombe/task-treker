from tasktreker.staff.models import Staff
from tasktreker.staff.forms import AddStaffForm, StaffUpdateForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.urls import reverse_lazy
# from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
User = get_user_model()


class AddStaffView(LoginRequiredMixin, CreateView):
    model = User
    form_class = AddStaffForm
    template_name = 'staff/add_new_staff.html'
    success_url = reverse_lazy('add_new_staff')

    '''def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)'''

    def get_success_url(self):
        return reverse("staff:add_new_staff")

    def form_valid(self, form):
        #form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS, "New staff details have been successfully added!")
        return super().form_valid(form)


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    form_class = StaffUpdateForm
    template_name = 'staff/staff_update_form.html'
    success_url = reverse_lazy('update_staff_details')

    def get_success_url(self):
        return reverse("staff:update_staff_details")  # , kwargs={"username": self.request.user.username})

    def get_object(self):
        return Staff.objects.get(user=self.request.user)

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        messages.add_message(self.request, messages.INFO, "The staff information have been successfully updated")
        return super().form_valid(form)
