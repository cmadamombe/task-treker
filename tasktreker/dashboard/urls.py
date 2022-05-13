from django.urls import path
from tasktreker.dashboard import views

app_name = "dashboard"

urlpatterns = [
    path("view/", views.DashboardView.as_view(), name="dashboard"),
]
