from django.db import models

from common_core.models import *

# Create your models here.
class Diary(BaseEntity, models.Model):
    
    diary_id = models.AutoField(primary_key=True)
    diary_name = models.CharField(max_length=40)


    def __str__(self):
        return 

    def __unicode__(self):
        return 
