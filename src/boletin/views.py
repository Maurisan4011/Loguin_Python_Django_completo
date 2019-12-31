from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

def inicio(request):
    titulo = "Bienvenidos"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    
    context = {
                "titulo": titulo,
                "el_form": form,
            }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "persona"
        instance.save()

        context = {
            "titulo" : "gracias %s!" %(nombre)
        }
        print (instance)
        print (instance.timestamp)

    
    return render(request, "inicio.html", context)

def contact(request):
    titulo = "Contacto"
    form =  ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = "form de contacto"
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
            )


    context = {
        "form" : form,
        "titulo" : titulo,
    }
    return render (request, "forms.html", context)