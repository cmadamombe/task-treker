from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, RedirectView, UpdateView
from tasktreker.users.forms import UserUpdateForm
from django.contrib import messages

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update_form.html'
    success_url = reverse_lazy('user_update')

    def get_success_url(self):
        return reverse("users:user_update") #kwargs={"username": self.request.user.username})

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        messages.add_message(self.request, messages.INFO, "To update personal details, please contact administrator!")
        return super().form_valid(form)


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

user_update_view = UserUpdateView.as_view()

user_redirect_view = UserRedirectView.as_view()
