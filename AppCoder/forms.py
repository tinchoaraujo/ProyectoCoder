from django import forms


class EquipoForm(forms.Form):
    nombre = forms.CharField()
    fundado = forms.IntegerField()


class BusquedaEquipoForm(forms.Form):
    nombre = forms.CharField()

