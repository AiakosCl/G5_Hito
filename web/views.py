from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm, ContactoForm
from .models import Productos, Contactos
from django.contrib import messages

# Create your views here.
# Vista para index.html
def index(request):
    productos = Productos.objects.filter(privado=False)
    return render(request, 'index.html',{'productos':productos})

# vista para about.html
def about(request):
    return render(request, 'about.html',{})

# Vista para welcome.html
def welcome(request):
    productos = Productos.objects.filter(privado=True)
    return render(request, 'welcome.html',{'productos':productos})

# Para crear un nuevo producto
def nuevo_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.save()
            messages.success(request, f'✅\tEl producto ha sido creado con éxito!')
            return redirect('DetalleProducto', slug=producto.slug)
        else:
            messages.warning(request,f'⛔\tPor favor, revisar la información faltante.')
    else:
        formulario = ProductoForm()
    return render(request, 'producto.html', {'formulario':formulario})

# Vista para ver el registro creado o modificado.
def detalle_producto(request, slug):
    producto = get_object_or_404(Productos, slug=slug)
    return render(request, 'detalle_producto.html', {'producto':producto})

# Vista para ver todos los productos creados, y que permitirá editarlos o borrarlos.
def lista_productos(request):
    productos = Productos.objects.all()
    return render(request, 'lista_productos.html',{'producto':productos})

def contact_view(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'✅\t¡Gracias por su contacto!')
            return redirect('Inicio')
        else:
            messages.warning(request,f'⛔\tPor favor, revisar la información ingresada.')
    else:
        formulario = ContactoForm()
    return render(request, 'contacto.html', {'contacto':formulario})