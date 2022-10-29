from django import forms
from django.forms import DateInput

from apps.administrador.models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        # fields = ('fechaPedido','cliente','menu','estadoPedido','comentario','envioDomicilio','tiempoDemora','cadete','total')
        fields = '__all__'

        widgets = {
            'fechaPedido': DateInput(format='%y-%m-%d', attrs={'type':'date'})
        }