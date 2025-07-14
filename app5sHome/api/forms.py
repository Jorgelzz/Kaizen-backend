from django import forms
from .models import Auditoria5S, User


class Auditoria5SForm(forms.ModelForm):
    class Meta:
        model = Auditoria5S
        fields = '__all__'

        