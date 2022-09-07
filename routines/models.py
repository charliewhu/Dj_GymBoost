from django.db import models
from django.urls import reverse

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("routine", kwargs={"pk": self.pk})
