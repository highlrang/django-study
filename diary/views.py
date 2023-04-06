from django.shortcuts import render
from rest_framework import viewsets
from diary.serializers import DiarySerializer
from diary.models import *


# Create your views here.
class DiaryView(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    # lookup_field
    # authentication_classes = [TokenAuthentication]
    # authentication_classes, permission_class ...

# get_object
# get_queryset 을 통해 동적으로 queryset 설정 가능



