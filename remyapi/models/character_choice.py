from django.db import models

class CharacterChoice(models.Model):
    """Model to keep track of character choices. These objects are flags to mark when notable events in the game has happened for a character, such as picking up an item, 
    to make sure you can't do the same major event twice."""

    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    choice = models.ForeignKey("Choice", on_delete=models.CASCADE)
    chosen = models.BooleanField(default=False) 

