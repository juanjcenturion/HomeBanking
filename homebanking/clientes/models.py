from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoCliente(models.Model):
    nombre = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        db_table = "tipo_cliente"

class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.DO_NOTHING)
    customer_name = models.CharField(max_length=50, blank=False)
    customer_surname = models.CharField(max_length=100, blank=False)
    customer_dni = models.IntegerField( blank=False)
    creation_date = models.DateField(default=datetime.now())
    
    def __str__(self):
        return f"USUARIO: {self.user}, TIPO_CLIENTE: {self.tipo_cliente}, NOMBRE_COMPLETO: {self.customer_name} {self.customer_surname}, DNI: {self.customer_dni}"
    
    class Meta:
        db_table = "cliente"