from django.shortcuts import render, get_object_or_404
from .models import Service


def home(request):
    return render(request, "services/index.html")


def service_list(request):
    services = Service.objects.all()
    return render(request, "services/service_list.html", {"services": services})


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, "services/service_detail.html", {"service": service})