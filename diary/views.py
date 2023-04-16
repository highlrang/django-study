from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from common_core.dtos import ApiResponse, ErrorCode
from diary.dtos import CategoryDiary
from diary.serializers import DiarySerializer, DiaryCategorySerializer
from common_core.exceptions import ApiException
from diary.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

import logging



# Create your views here.
class DiaryView(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    # lookup_field
    # authentication_classes = [TokenAuthentication]
    # authentication_classes, permission_class ...

    def list(self, request, *args, **kwargs):

        diary_list = Diary.objects.all().order_by('start_date', 'end_date')
        return ApiResponse.success(diary_list)
        # return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']

        logger = logging.getLogger('django')
        logger.info('로그내용')
        logging.error('======에러 발생======')

        diary = self.get_object()
        serializer = DiarySerializer(diary)
        
        print(serializer.data)

        return Response({"data": serializer.data})
    
        


# get_object pk detail
# get_queryset 을 통해 동적으로 queryset 설정 가능

class CategoryDiaryView(viewsets.ViewSet): # LoginRequiredMixin
    serializer_class = DiaryCategorySerializer #(many=True)

    def retrieve(self, request, *args, **kwargs):
        raise ApiException(ErrorCode.DATA_NOT_FOUND)
    

    # @action(detail=False, methods=['post'])
    def create(self, request):
        print(request)
        print(request.data)
        
        apiResponse = ApiResponse()

        serializer = DiaryCategorySerializer(data = request.data)
        
        print(serializer.is_valid())
        if serializer.is_valid():
            category_name = request.data['category_name']
        
            print(request.user)
            print(DiaryCategory.objects.exists(user_id=request.user, category_name=category_name))

            DiaryCategory.objects.exists(user_id=request.user, category_name=category_name)

            # if category 존재 안 하면 
            # diaryCategory = DiaryCategory.objects.create(category_name = category_name)
            

            diary = Diary.objects.create(diary_name = request.data['diary_name'])
            # category_id
            apiResponse = ApiResponse.success(diary)

        return Response(apiResponse.__dict__)

        # Diary 및 Category 저장
        # CategoryDiary()
        return Response()
    




