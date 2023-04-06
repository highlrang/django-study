from django.db import models

from common_core.models import BaseEntity

# Create your models here.
class Diary(BaseEntity):
    
    category_id = models.IntegerField()
    diary_id = models.AutoField(primary_key=True)
    diary_name = models.CharField(max_length=40)

class UserCategory(BaseEntity):

    user_id = models.IntegerField()
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=40)
    parent_category_id = models.IntegerField()
