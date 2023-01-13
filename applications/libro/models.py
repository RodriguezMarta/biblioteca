from django.db import models
from django.db.models.signals import post_save

# apps tercero
from PIL import Image

# from local apps
from applications.autor.models import Autor
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name='categoria_libro'
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada', null=True)

    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return str(self.id) + '-' + self.titulo


def optimize_image(sender, instance, **kwargs):
    print("  ==================== ")
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)



post_save.connect(optimize_image, sender=Libro)
