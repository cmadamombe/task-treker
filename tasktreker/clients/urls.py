from django.urls import path
from tasktreker.clients import views

app_name = "clients"

urlpatterns = [
    path("add/new/", views.AddClientView.as_view(), name="add_new_client"),
    path("update/", views.ClientUpdateView.as_view(), name="update_client_details"),
]

