from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"

class Vehiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    anio = models.IntegerField()
    dominio = models.CharField(max_length=10)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.anio} - {self.dominio}"
    
    