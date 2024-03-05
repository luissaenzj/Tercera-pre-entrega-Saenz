from django.shortcuts import render
from django.http import HttpResponse
from OwnApp.models import *
from OwnApp.forms import *

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def busqueda(request):

    if request.GET:
    
        nombre = request.GET["nombre"]
        user = Usuario.objects.filter(nombre__icontains=nombre)
    
        mensaje =f'Estamos buscando al usuario {nombre}'

        return render(request, "busqueda.html",{"mensaje":mensaje,"resultados":user})

    return render(request, "busqueda.html") #si todavia no hay una busqueda

## Vistas de Creacion

def crear_producto (request): #Forma de crear formulario sin Forms

    if request.method == 'POST':

        crear_producto = Producto(nombre=request.POST["n_producto"],
                                  categoria=request.POST["n_categoria"],
                                  codigo=request.POST["codigo"]
                                  )
        crear_producto.save()

        return render(request, "inicio.html")



    return render(request, "crear_producto.html")


def crear_usuario (request): #Forma de crear formulario con Forms

    if request.method == 'POST':

        formulario = UsuarioForm (request.POST)

        if formulario.is_valid ():

            info_dic = formulario.cleaned_data

            usuario_nuevo = Usuario(nombre=info_dic["nombre"],
                                    apellido=info_dic["apellido"],
                                    email=info_dic["email"],
                                    edad=info_dic["edad"])

            usuario_nuevo.save()

            return render(request, "inicio.html")
        
    else:

        formulario = UsuarioForm()
    
    return render(request, "crear_usuario.html",{"formu":formulario})


def crear_requerimiento (request):

    if request.method == 'POST':

        formulario = RequerimientoForm (request.POST)

        if formulario.is_valid ():

            info_dict = formulario.cleaned_data

            req_nuevo = Requerimiento(req=info_dict["req"],
                                    fechaReq=info_dict["fechaReq"],
                                    UserPro=info_dict["UserPro"])

            req_nuevo.save()

            return render(request, "inicio.html")
        
    else:

        formulario = RequerimientoForm()
    
    return render(request, "crear_req.html",{"formq":formulario})

