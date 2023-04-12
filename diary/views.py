from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action
from common_core.dtos import ApiResponse
from diary.dtos import CategoryDiary
from diary.serializers import DiarySerializer, DiaryCategorySerializer
from diary.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DiaryView(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    # lookup_field
    # authentication_classes = [TokenAuthentication]
    # authentication_classes, permission_class ...

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        diary = self.get_object()
        serializer = DiarySerializer(diary)
        
        print(serializer.data)
        Response(serializer.data)
        return Response({"data": serializer.data})
        


# get_object pk detail
# get_queryset 을 통해 동적으로 queryset 설정 가능

class CategoryDiaryView(LoginRequiredMixin, viewsets.ViewSet):
    serializer_class = DiaryCategorySerializer #(many=True)

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

        return Response(apiResponse)

        # Diary 및 Category 저장
        # CategoryDiary()
        return Response()
    




