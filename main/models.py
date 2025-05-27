from django.db import models
from django.db.models import CASCADE


class Togri(models.Model):
    soz = models.CharField(max_length=255)

    def __str__(self):
        return self.soz
    class Meta:
        verbose_name_plural = "Togri so'zlar "

class Notogri(models.Model):
    soz = models.CharField(max_length=255)
    togri = models.ForeignKey(Togri, on_delete=CASCADE)

    def __str__(self):
        return self.soz

    class Meta:
        verbose_name_plural = "Notogri so'zlar "