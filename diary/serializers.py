from rest_framework import serializers
from django.contrib.auth import models
from django.contrib.auth.mixins import LoginRequiredMixin

from diary.models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary 
        fields = ('diary_id', 'diary_name')

class DiaryCategorySerializer(LoginRequiredMixin, serializers.Serializer):
    category_name = serializers.CharField()
    diary_name = serializers.CharField()

    def create(self, validated_data):
        return super().create(validated_data)
    
    # 카테고리 하나에 여러 일정들 일대다 관계이기 때문에 중간 테이블 X
    # 카테고리만 생성할 수도 있지
    # 다이어리 생성할 때 카테고리 정보 넣어서 없을 경우 category create까지
    