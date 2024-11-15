from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email