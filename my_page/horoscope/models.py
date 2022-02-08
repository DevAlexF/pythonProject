from django.db import models


class Zodiac(models.Model):
    name = models.CharField(max_length=200)
    information = models.TextField(max_length=5000)

    def __str__(self):
        return self.name


    # def __str__(self):
    #     return self.information