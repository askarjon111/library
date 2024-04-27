from django.db import models
from django.db.models import Q


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(~Q(covers=None))
