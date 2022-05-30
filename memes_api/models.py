from django.db import models
from django.contrib.auth import get_user_model

class Meme(models.Model):
    """
    Model representing a single meme.
    """
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='memes_imgs')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name