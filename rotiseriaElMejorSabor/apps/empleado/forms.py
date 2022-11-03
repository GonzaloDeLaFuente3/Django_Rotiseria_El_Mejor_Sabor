from django import forms
from django.forms import DateInput
from apps.empleado.models import Empleado
from apps.cadete.models import Cadete


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'

        widgets = {
            'fechaIngreso': DateInput(format='%y-%m-%d', attrs={'type':'date'}),
            'fechaNacimiento': DateInput(format='%y-%m-%d', attrs={'type': 'date'})
        }

class CadeteForm(forms.ModelForm):

    class Meta:
        model = Cadete
        fields = '__all__'

        widgets = {
            'vigenciaCarnet': DateInput(format='%y-%m-%d', attrs={'type':'date'}),
            'fechaIngreso': DateInput(format='%y-%m-%d', attrs={'type': 'date'}),
            'fechaNacimiento': DateInput(format='%y-%m-%d', attrs={'type': 'date'})
        }