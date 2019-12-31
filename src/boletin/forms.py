from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]

        def clean_email(self):
            email = self.cleaned_data.get("email")
            return email

        def clean_nombre(self):
            nombre = self.cleaned_data.get("nombre")
            # validaciones
            return nombre

class ContactForm(forms.Form):
    nombre = forms.CharField(required=False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
