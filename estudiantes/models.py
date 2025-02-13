from django.db import models

class Estudiante(models.Model):
    carnetcarrera = models.IntegerField()
    carnetanio = models.IntegerField()
    carnetcorrelativo = models.IntegerField()
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    pagado = models.BooleanField(default=False)
    fecharegistro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre1} {self.nombre2} {self.apellido1} {self.apellido2}"
