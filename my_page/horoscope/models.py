from django.db import models


class Zodiac(models.Model):
    name = models.CharField(max_length=200)
    information = models.TextField(max_length=5000)
    # st = models.DateField()
    # fd = models.DateField()

    def __str__(self):
        return self.name