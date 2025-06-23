from django.db import models
from clients.models import Client


# Estados de pago
# Estado general (activo/inactivo)
ACTIVE = 1
INACTIVE = 0

STATE_CHOICES = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
]

# Estado de pago del servicio
PAYMENT_PENDING = 0
PAYMENT_COMPLETE = 1
PAYMENT_PARTIAL = 2
PAYMENT_STATUS_CHOICES = [
    (PAYMENT_PENDING, 'Pending'),
    (PAYMENT_COMPLETE, 'Paid'),
    (PAYMENT_PARTIAL, 'Partially Paid'),
]



class ServiceType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    base_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Tarifa base
    state = models.SmallIntegerField(choices=STATE_CHOICES, default=ACTIVE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'service_type'  #  

    def __str__(self):
        return self.name


class Service(models.Model):
    client = models.ForeignKey(Client,related_name='services', on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType,related_name='services', on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    custom_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateField()
    payment_status  = models.SmallIntegerField(choices=PAYMENT_STATUS_CHOICES)
    state = models.SmallIntegerField(choices=STATE_CHOICES, default=ACTIVE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'service'


    def __str__(self):
        return f"{self.client.name} - {self.service_type.name} ({self.date})"