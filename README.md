# Rockfit
![rock fit](https://user-images.githubusercontent.com/50236187/211225885-247a05c5-adcf-4051-9328-8b0267a249af.png)

# 조원소개
김락형, 김세은, 송원준, 유소연, 이민지, 이정연, 정지호

# 서비스소개
![포스터](https://user-images.githubusercontent.com/50236187/211225909-5789b0f8-b6c4-43c0-b7d2-e08bf7ff9bbb.jpg)


# 패키지 설치
pip install -r requirements.txt

# DB 연동
cd game
python manage.py makemigrations mainapp
python manage.py migrate mainapp
python manage.py makemigrations core
python manage.py migrate core
python manage.py migrate

# 서버 실행
python manage.py runserver

# 게임 실행
http://localhost:8000/mainapp/main

# 관리자 계정
python manage.py createsuperuser
http://localhost:8000/admin
