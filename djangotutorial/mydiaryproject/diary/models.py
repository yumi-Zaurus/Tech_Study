from django.db import models
from django.utils import timezone
import uuid

# Create your models here.


class Diary(models.Model):
    id = models.UUIDField()