from django.shortcuts import render
from rest_framework import generics
from diary.serializers import DiarySerializer
from diary.models import *


# Create your views here.
class DiaryAPI(generics.CreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    # authentication_classes = [TokenAuthentication]
    # authentication_classes 및 filter에서 담당하기

'''
    def get(self, request, *args, **kwargs):
        print("get 요청")
        print(request)
        print(*args)
        print(**kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('post 요청')
        print(request)
        print(*args)
        print(**kwargs)
        return super().post(request, *args, **kwargs)
'''
    

