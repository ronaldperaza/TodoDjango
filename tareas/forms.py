from django import forms
from django.forms import ModelForm
from .models import *

class FormTarea(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = '__all__'