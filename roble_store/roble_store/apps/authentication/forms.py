from django import forms
from .models import Clientes


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('email','nombres','telefonouno')
