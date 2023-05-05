from django.db import models


class followers(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name
