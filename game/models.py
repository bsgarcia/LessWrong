from django.db import models


class Propositions(models.Model):
    accessible = models.BooleanField()
    complete = models.BooleanField()
    proposition = models.PositiveIntegerField()
    answer = models.BooleanField()

