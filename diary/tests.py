import json
from django.test import TestCase
from django.urls import reverse
import mock
import unittest

from .models import diary

# Create your tests here.
class DiaryAPITests(TestCase):

    # 테스트 데이터
    def setUp(self):
        diary.objects.get_or_create(diary_name='테스트일정')

    def test_list(self):
        url = reverse("") # ??
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(len(data), 1)
        self.assertContains(data, '테스트일정')