from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    """Model to create a single character. One user can have several characters - this is kind of like a save file for a single play through."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="characters")
    first_name= models.CharField(max_length=25)
    current_situation = models.ForeignKey("Situation", on_delete=models.CASCADE, related_name="characters")
    items = models.ManyToManyField("Item", related_name="characters")