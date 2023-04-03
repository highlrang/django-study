
from django.urls import include, path
from diary import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'v1', DiaryAPI)

urlpatterns = [
    path('', views.DiaryAPI.as_view(), name='')
]

