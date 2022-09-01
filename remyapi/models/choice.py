from django.db import models

class Choice(models.Model):
    """Model for a single choice. This is an option that the user will be able to choose for a situation. Once situation will have multiple choices associated with it."""

    situation = models.ForeignKey("Situation", on_delete=models.CASCADE, related_name="resulting_choices")
    text = models.TextField()
    outcome_situation = models.ForeignKey("Situation", on_delete=models.CASCADE, related_name="previous_choices")
    get_item_bool = models.BooleanField(default=False)
    new_item = models.ForeignKey("Item", on_delete=models.CASCADE, related_name = "find_item_choices")
    required_item_bool = models.BooleanField(default=False)
    required_item = models.ForeignKey("Item", on_delete=models.CASCADE, related_name="use_item_choices")