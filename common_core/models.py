from datetime import datetime
from django.db import models


class BaseEntity(models.Model):
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    insert_operator = models.CharField(default='SYSTEM', max_length=20)
    update_operator = models.CharField(default='SYSTEM', max_length=20)
    delete_yn = models.CharField(default='N', max_length=1)

    class Meta:
        abstract = True