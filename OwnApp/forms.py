from django import forms


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    codigo = forms.IntegerField()

class UsuarioForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    edad= forms.IntegerField()

class RequerimientoForm (forms.Form):
    req= forms.CharField(max_length=50)
    fechaReq= forms.DateField()
    UserPro = forms.BooleanField()

   