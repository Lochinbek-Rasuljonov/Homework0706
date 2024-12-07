from django.db import models
import os

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    AUTOMATIC = 'Automatic'
    MANUAL = 'Manual'
    TRANSMISSION_CHOICES = [
        (AUTOMATIC, 'Automatic'),
        (MANUAL, 'Manual'),
    ]

    PETROL = 'Petrol'
    DIESEL = 'Diesel'
    ELECTRIC = 'Electric'
    ENGINE_CHOICES = [
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel'),
        (ELECTRIC, 'Electric'),
    ]

    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=50, choices=ENGINE_CHOICES)
    mileage = models.IntegerField()
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)

    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Car.objects.get(pk=self.pk).image
            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name