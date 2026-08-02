from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.service_list, name="service_list"),
    path("services/<int:id>/", views.service_detail, name="service_detail"),
    path("book/", views.book_appointment, name="book_appointment"),
    path("appointments/", views.appointment_list, name="appointment_list"),

    path(
        "appointments/<int:id>/update/",
        views.update_appointment_status,
        name="update_status",
    ),
]