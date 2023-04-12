from rest_framework import serializers
from django.contrib.auth import models
from django.contrib.auth.mixins import LoginRequiredMixin

from diary.models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary 
        fields = ('diary_id', 'diary_name')

class DiaryCategorySerializer(LoginRequiredMixin, serializers.Serializer): 
    category_name = serializers.CharField(max_length=30)
    diary_name = serializers.ListField(child=DiarySerializer())

    # diary = DiarySerializer() # 각 필드에 직렬정의 가능
    
    '''
    {
"category_name": "test",
"diary_name": [
{
"diary_name": "d1"
}
]
}
    '''
    