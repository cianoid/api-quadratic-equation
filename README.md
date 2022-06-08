# api-quadratic-equation
Тестовое задание для БО-Энерго. Сервис по решению квадратных уравнений


# Клонирование репозиотрия

```
git clone https://github.com/cianoid/api-quadratic-equation.git
```

# Создание .env-файла

Создайте .env-файлы в папке ```api-quadratic-equation/quadratic```

Пример заполнения файла:
```
SECRET_KEY=django-seeetre-raskljdio23452o3@#$R$@TG%$
DEBUG=0
ALLOWED_HOSTS=localhost
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

# Запуск в dev-режиме

Предусмотрено два варианта запуска сервиса. В dev-режиме и в режиме контейнера Docker

## Установка venv с зависимостями

```
cd api-quadratic-equation

# для Linux, MacOS
python3 -m venv venv
source venv/bin/activate

# для Windows
python -m venv venv
venv/Scripts/activate

python -m pip install --upgrade pip
cd quadratic
pip install -r requirements.txt
```

## Миграции БД и запуск сервиса 

```
python manage.py migrate
python manage.py runserver localhost:8080
```

## Запуск тестов
```
python maange.py test
```

# Запуск в контейнере Docker

```
docker build -t quadratic_equation .
docker run --name quadratic_equation -d -p 8000:8000 quadratic_equation
```

# Автор
Шатава Игорь, Python-разработчик
