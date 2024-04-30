from django.shortcuts import render

# Create your views here.
def index(request):
    datos = {
        'nombre': 'Gerardo Alvarez',
        'RUT': '13869385-6',
        'correo':'gerardo.alvarez@outlook.com'}
    return render(request, 'index.html',{'info':datos})

def about(request):
    return render(request, 'about.html',{})

def welcome(request):
    return render(request, 'welcome.html',{})

