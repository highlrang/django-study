
from django.urls import include, path
from diary import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'diary', views.DiaryView, 'diary')
router.register(r'diary-category', views.CategoryDiaryView, 'diary-category')

urlpatterns = [
    path('', include(router.urls)),
    # path('create_all', views.CategoryDiaryView.as_view({'post': 'create_all'}))
]

