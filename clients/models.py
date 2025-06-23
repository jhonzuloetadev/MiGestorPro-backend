from django.db import models


# Estado del cliente
ACTIVE = 1
INACTIVE = 0
STATE_CHOICES = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
]

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=15, unique=True)  # DNI o RUC
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.SmallIntegerField(choices=STATE_CHOICES, default=ACTIVE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'client'  #  

    def __str__(self):
        return self.name
