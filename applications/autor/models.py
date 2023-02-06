from datetime import date
from django.db import models
from django.db.models import Q,F


class Persona(models.Model):
    nombres = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacimiento = models.DateField(null=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return str(self.id) + '-' + self.nombres + '-' + self.apellidos



class Autor(Persona):
    muerte = models.DateField(null=True, blank=True)
    edad = models.IntegerField(blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.muerte != None:
            edad = self.muerte.year - self.nacimiento.year - ((self.muerte.month, self.muerte.day) < (self.nacimiento.month, self.nacimiento.day))
        else:
            today = date.today()
            edad = today.year - self.nacimiento.year - ((today.month, today.day) < (self.nacimiento.month, self.nacimiento.day))
        self.edad= edad
        super(Autor, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores' 
        constraints = [
            models.CheckConstraint(
                check=models.Q(nacimiento__lte=models.F("muerte")),
                name="error"),
                ] 