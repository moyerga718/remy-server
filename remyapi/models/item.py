from django.db import models

class Item(models.Model):
    """Model for one item. User can pick up items throughout journey - these will be added to the characters inventory (join table between character and items)"""

    name = models.CharField(max_length=35)
    description = models.TextField()
    starting_item = models.BooleanField(default=False)