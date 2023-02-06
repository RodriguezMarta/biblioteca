from django.contrib.gis.db import models
from django.utils import timezone
import datetime

from .models import Prestamo

def borrar_antigusos(self):
    if self.fecha_devolucion < datetime.datetime.now()-datetime.timedelta(days=7):
        e = Prestamo.objects.get(pk=self.pk)
        e.delete()
        return True
    else:
        return False