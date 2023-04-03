from rest_framework import serializers

from diary.models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary 
        fields = ('diary_id', 'diary_name')