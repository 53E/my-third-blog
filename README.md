# Django 이미지 블로그와 REST API

## 프로젝트 개요
이 프로젝트는 Django를 사용하여 이미지 업로드 기능이 있는 블로그와 REST API를 구현한 것입니다.

## 주요 기능
- 이미지 업로드가 가능한 블로그 포스트
- Django REST Framework를 사용한 API
- 토큰 기반 인증
- 반응형 웹 디자인

## 설치 및 실행

### 1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 슈퍼유저 생성
```bash
python manage.py createsuperuser
```

### 5. 서버 실행
```bash
python manage.py runserver
```

## API 사용법

### 토큰 생성
```bash
python manage.py drf_create_token [username]
```

### API 엔드포인트
- 블로그 메인: http://127.0.0.1:8000/
- 관리자 페이지: http://127.0.0.1:8000/admin/
- REST API: http://127.0.0.1:8000/api_root/
- 토큰 인증: http://127.0.0.1:8000/api-token-auth/

### CURL을 이용한 API 테스트
```bash
curl -X POST -S \
-H "Authorization: JWT [토큰]" \
-H 'Accept: application/json' \
-F "title=제목" \
-F "text=내용" \
-F "created_date=2023-06-07T18:34:00+09:00" \
-F "published_date=2023-06-07T18:34:00+09:00" \
-F "image=@/path/to/image.jpg;type=image/jpg" \
http://127.0.0.1:8000/api_root/Post/
```

## 프로젝트 구조
```
my-second-blog-main/
├── myblog/
│   ├── migrations/
│   ├── static/css/
│   ├── templates/myblog/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── media/
├── requirements.txt
└── manage.py
```

## 변경사항
- blog 앱을 myblog로 변경
- 이미지 필드 추가
- REST API 기능 추가
- 토큰 기반 인증 추가
