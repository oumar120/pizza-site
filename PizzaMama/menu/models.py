from django.db import models

# Create your models here.
class Pizza(models.Model) :
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    print = models.FloatField(default=0)
    vegetarien = models.BooleanField(default=False)

    def __str__(self):
        return self.nom