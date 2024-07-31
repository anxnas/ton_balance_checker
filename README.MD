# TON Balance Checker

Это веб-приложение на Django для проверки баланса TON кошелька. Приложение позволяет пользователям вводить адрес кошелька и получать информацию о балансе, последней активности и статусе кошелька.

## Функциональность

- Ввод адреса TON кошелька
- Получение баланса кошелька
- Отображение последней активности кошелька
- Отображение статуса кошелька (active/inactive)

## Требования

- Python 3.9+
- Django 3.2+
- Docker
- Docker Compose

## Установка и запуск

### Локальная установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/yourusername/ton_balance_checker.git
    cd ton_balance_checker
    ```

2. Создайте и активируйте виртуальное окружение:

    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Запустите сервер разработки:

    ```sh
    python manage.py runserver
    ```

5. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/`.

### Использование Docker

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/yourusername/ton_balance_checker.git
    cd ton_balance_checker
    ```

2. Соберите и запустите контейнеры с помощью Docker Compose:

    ```sh
    docker-compose up --build
    ```

3. Откройте браузер и перейдите по адресу `http://localhost:8000/`.

## Тестирование

Для запуска тестов используйте команду:

   ```sh
   python manage.py test app
   ```


## Структура проекта

- `app/`: Приложение Django для проверки баланса кошелька
  - `forms.py`: Форма для ввода адреса кошелька
  - `views.py`: Представления для обработки запросов
  - `urls.py`: URL маршруты приложения
  - `templates/balance/index.html`: Шаблон для отображения формы и результатов
  - `static/css/style.css`: Стили для веб-приложения TON Balance Checker
  - `tests.py`: Тесты для приложения
- `ton_balance_checker/`: Основной проект Django
  - `settings.py`: Настройки проекта
  - `urls.py`: Основные URL маршруты проекта
- `Dockerfile`: Описание Docker образа
- `docker-compose.yml`: Конфигурация Docker Compose
- `requirements.txt`: Зависимости проекта

## Пример использования

1. Введите адрес кошелька в поле ввода.
2. Нажмите кнопку "Найти".
3. Приложение отобразит баланс кошелька, последнюю активность и статус.

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

## Авторы

- Хренов Святослав (anxnas)
