# auction_demo

### База данных
    docker-compose up -d --build

### Сервер разработки
    python src/manage.py runserver

### Celery
    celery -A auction worker -Q default,email
