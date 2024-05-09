from django.db import models
from django.utils.text import slugify
import uuid #Para crear UUID automáticos, hay que dejarlos en default=uuid.uuid4 en el campo que sea del tipo

# Create your models here.
class Productos(models.Model):
    estado = (
        (True, 'Privado'),
        (False, 'Público')
    )
    azucar = (
        (True, 'Sin azúcar'),
        (False, 'Tradicional')
    )

    id_producto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=64, blank=False, unique=True)
    descripcion = models.TextField(blank=False)
    # imagen = models.URLField(default='https://acortar.link/PJ8L3Y')
    imagen = models.ImageField(upload_to='productos/', default='productos/cargar_imagen.png')
    slug = models.SlugField(unique=True, blank=True)
    precio = models.DecimalField(blank=False, decimal_places=0, max_digits=10, default=0)
    liviano = models.BooleanField(choices=azucar, blank=False, default=False)
    privado = models.BooleanField(choices=estado, blank=False, default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.nombre)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.nombre

class Contactos(models.Model):
    ContactoId = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    NombreCliente= models.CharField(max_length=64, blank=False, null=True)
    EmailCliente = models.EmailField(max_length=50, blank=False, null=True)
    Mensaje = models.TextField(blank=False)

    def __str__(self) -> str:
        return self.NombreCliente