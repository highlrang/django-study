import unittest
from unittest import mock
from unittest.mock import Mock, MagicMock
from diary.views import DiaryView
from diary.models import *
from datetime import datetime
import datetime as dt
# from django.test import TestCase

class DiaryUnitTest(unittest.TestCase):

    @mock.patch('diary.models.Diary.objects')
    def test_diary_sort(self, diaryQueryset):
        
        # 정렬된 배열
        start_date = datetime(2023, 4, 15)
        
        diary1 = MagicMock()
        diary1.start_date = start_date
        diary1.end_date = start_date + dt.timedelta(days = 3)

        diary2 = MagicMock()
        diary2.start_date = start_date
        diary2.end_date = start_date + dt.timedelta(days = 5)

        raw_list = [diary2, diary1]
        
        sorted_list = sorted(raw_list, key = lambda d: (d.start_date, d.end_date))

        # service 로직 나눌 필요 있음
        diaryQueryset.all.return_value.order_by.return_value = sorted_list

        # 정렬 메서드 호출
        diaryView = DiaryView()
        return_list = diaryView.list(Mock()).data

        # TestCase 메서드 self로 이용
        self.assertEqual(len(sorted_list), len(return_list))
        self.assertEqual(sorted_list[0].start_date, return_list[0].start_date)
        self.assertEqual(sorted_list[1].end_date, return_list[1].end_date)
