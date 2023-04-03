from django.db import models


class BaseEntity(models.Model):
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    insert_operator = models.CharField(default='SYSTEM', max_length=20)
    update_operator = models.CharField(default='SYSTEM', max_length=20)
    delete_yn = models.BooleanField(default=False)

    class Meta:
        abstract = True