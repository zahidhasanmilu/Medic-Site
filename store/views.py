from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Service, Contact
from .forms import ContactForm

from django.contrib import messages
# Create your views here.


def home(request):
    service = Service.objects.all()

    context = {
        'services': service
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to the database if valid
#             return redirect('home')# Redirect to a success page or perform other actions
#     else:
#         form = ContactForm()

#     context = {
#         'forms': form
#     }
#     return render(request, 'contact.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contactobj = Contact(name=name, email=email,
                             phone=phone, message=message)
        contactobj.save()
        messages.success(request, 'message send successfully ')
        return redirect('contact')


    return render(request, 'contact.html',)
