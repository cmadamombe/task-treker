from django.urls import path
from tasktreker.staff import views

app_name = "staff"

urlpatterns = [
    path("add/new/", views.AddStaffView.as_view(), name="add_new_staff"),
    path("update/", views.StaffUpdateView.as_view(), name="update_staff_details"),
]

