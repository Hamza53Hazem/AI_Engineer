from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import ContactMessage, Service, Testimonial


def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    testimonials = Testimonial.objects.filter(is_featured=True)[:3]
    context = {
        "services": services,
        "testimonials": testimonials,
    }
    return render(request, "main/home.html", context)


def about(request):
    return render(request, "main/about.html")


def services(request):
    services = Service.objects.filter(is_active=True)
    return render(request, "main/services.html", {"services": services})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! We will reply soon.")
            return redirect(reverse("contact_success"))
    else:
        form = ContactForm()

    return render(request, "main/contact.html", {"form": form})


def contact_success(request):
    return render(request, "main/contact_success.html")
