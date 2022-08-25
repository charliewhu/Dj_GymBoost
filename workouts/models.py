from django.db import models
from django.urls import reverse

# Create your models here.
class Workout(models.Model):
    def get_absolute_url(self):
        return reverse("workout", kwargs={"pk": self.pk})
