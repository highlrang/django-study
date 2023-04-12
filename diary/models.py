from django.db import models

from common_core.models import BaseEntity

# Create your models here.

# user 하나에 여러 Diary
# diary 하나에 한 User
# user 하나에 여러 Category
# category 하나에 여러 diary
# diary 하나에 한 Category

# ===== user =====
# category category
# diary diary diary

class Diary(BaseEntity):
    
    category_id = models.IntegerField(null=True)
    diary_id = models.AutoField(primary_key=True)
    diary_name = models.CharField(max_length=40)

class DiaryCategory(BaseEntity):
    user_id = models.IntegerField(default=0)
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=40)
    parent_category_id = models.IntegerField()

