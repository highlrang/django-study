from dataclasses import dataclass

@dataclass # 생성자 필요없음
class CategoryDiary:
    category_id: int
    category_name: str
    diary_name: str

    