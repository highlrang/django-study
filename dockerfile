# 베이스 이미지 설정
FROM python:3.8

WORKDIR /diary-project

# 가상환경
RUN python3.8 -m venv env
RUN /bin/bash -c "source env/bin/activate"

# 패키지 설치
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 프로젝트 폴더 생성
WORKDIR /diary-project/diary

COPY diary/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]