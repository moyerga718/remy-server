from django.db import models

class CharacterChoice(models.Model):
    """Model to keep track of character choices. These objects are flags to mark when notable events in the game has happened for a character, such as picking up an item, 
    to make sure you can't do the same major event twice."""

    character = models.ForeignKey("Character", on_delete=models.CASCADE, related_name="character_choices")
    choice = models.ForeignKey("Choice", on_delete=models.CASCADE, related_name="character_choices")
    chosen = models.BooleanField(default=False) 

