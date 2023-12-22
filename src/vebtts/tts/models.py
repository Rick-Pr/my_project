from django.db import models


class Txt(models.Model):
    name = models.CharField(max_length=100000)

    def __str__(self):
        return self.name
