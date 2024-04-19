from django.conf import settings
from django.db import models


class TestModel(models.Model):
    "Generated Model"
    test = models.TextField()
