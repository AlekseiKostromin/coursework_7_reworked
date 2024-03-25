# Курсовая работа №7 (DRF)

API-Сервис для помощи в приобретении полезных привычек
Сервис помогает создавать новые полезные привычки. Вы можете создать новую полезную привычку,
указать периодичность её выполнения, время для выполнения и место. Также реализована рассылка
напоминаний о выполнении через telegram-bot(Для этого при регистрации нужно указать ваш telegram id).

-Настроен CORS.
-Настроена интеграцию с Telegram.
-Реализована пагинация.
-Все необходимые модели описаны или переопределены.
-Реализованы CRUD эндпоинты.
-Описанные права доступа заложены.
-Отложенные задачи реализованы через Celery и Celery Beat.
-Все необходимые валидаторы настроены.
-Покрытие тестами 80%.
-Результат проверки Flake8 равен 100%, при исключении миграций.
-Для работы в виртуальном окружении требования указаны в файле requirements.txt.
-Для работы проекта необходимо настроить No-SQL СУБД Redis

## Запуск проекта через Docker

Cобрать образ командой docker-compose build
Запустить контейнер командой docker-compose up

## Документация API

Документация API доступна после запуска сервера по адресу:
http://localhost:8000/redoc/ или
http://localhost:8000/swagger/