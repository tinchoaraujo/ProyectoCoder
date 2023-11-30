from django import forms


class EquipoForm(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()

class BusquedaEquipoForm(forms.Form):
    nombre = forms.CharField()