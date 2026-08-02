from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Appointment
from .forms import CustomerForm, AppointmentForm



def home(request):
    return render(request, "services/index.html")


def service_list(request):
    services = Service.objects.all()
    return render(request, "services/service_list.html", {"services": services})


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, "services/service_detail.html", {"service": service})


def book_appointment(request):

    selected_service = request.GET.get("service")

    if request.method == "POST":

        customer_form = CustomerForm(request.POST)
        appointment_form = AppointmentForm(request.POST)

        if customer_form.is_valid() and appointment_form.is_valid():

            customer = customer_form.save()

            appointment = appointment_form.save(commit=False)
            appointment.customer = customer
            appointment.save()

            return render(
                request,
                "services/booking_success.html",
                {
                    "customer": customer,
                    "appointment": appointment,
                }
            )

    else:

        customer_form = CustomerForm()

        if selected_service:
            appointment_form = AppointmentForm(
                initial={"service": selected_service}
            )
        else:
            appointment_form = AppointmentForm()


    return render(
        request,
        "services/book_appointment.html",
        {
            "customer_form": customer_form,
            "appointment_form": appointment_form,
        }
    )

@login_required
def appointment_list(request):

    status_filter = request.GET.get("status")

    if status_filter:
        appointments = Appointment.objects.filter(
            status=status_filter
        )
    else:
        appointments = Appointment.objects.all()


    total_appointments = Appointment.objects.count()

    pending_count = Appointment.objects.filter(
        status="Pending"
    ).count()

    confirmed_count = Appointment.objects.filter(
        status="Confirmed"
    ).count()

    completed_count = Appointment.objects.filter(
        status="Completed"
    ).count()


    return render(
        request,
        "services/appointment_list.html",
        {
            "appointments": appointments,
            "selected_status": status_filter,

            "total_appointments": total_appointments,
            "pending_count": pending_count,
            "confirmed_count": confirmed_count,
            "completed_count": completed_count,
        }
    )
@login_required
def update_appointment_status(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == "POST":

        new_status = request.POST.get("status")

        appointment.status = new_status

        appointment.save()

        return redirect("appointment_list")


    return render(
        request,
        "services/update_status.html",
        {
            "appointment": appointment
        }
    )