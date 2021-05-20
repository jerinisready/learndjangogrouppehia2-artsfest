from django.db import models


class Event(models.Model):

    name = models.CharField(max_length=120)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", ]





