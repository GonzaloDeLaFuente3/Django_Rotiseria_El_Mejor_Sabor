from django import forms
from django.forms import DateInput
from apps.empleado.models import Empleado


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'

        widgets = {
            'fechaIngreso': DateInput(format='%y-%m-%d', attrs={'type':'date'})
        }