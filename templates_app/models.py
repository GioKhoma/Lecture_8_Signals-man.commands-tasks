from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
