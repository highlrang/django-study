import unittest;
import mock;

class DiaryUnitTest(unittest.TestCase):
    
    @mock.patch.object(, "get_diary"):
    def diary_sort_test(self, get_diary):
        
        # 정렬된 배열
        expect_result = []

        # 정렬 전 데이터 mocking
        get_diary.return_value = []

        # 정렬 메서드 호출
        sorted_result = mock으로 제공했던 get_diary를 실제로 정렬허는 메서드


        self.assertEqual(sorted_result, expect_result)