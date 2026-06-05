# Автотесты REST API Яндекс.Диска

Пример проекта автотестов для [REST API Яндекс.Диска](https://yandex.ru/dev/disk/rest/).  
Тесты выполняются против боевого API (`https://cloud-api.yandex.net`) с OAuth-токеном из [Полигона](https://yandex.ru/dev/disk/poligon/) — **личный аккаунт не требуется**.

## Стек

- Python 3
- [pytest](https://github.com/pytest-dev/pytest)
- [requests](https://github.com/psf/requests)
- python-dotenv (загрузка переменных окружения)

## Покрытие HTTP-методов

| Метод  | Эндпоинт API                    | Тест                          |
|--------|---------------------------------|-------------------------------|
| GET    | `/v1/disk`                      | `tests/test_get.py`           |
| GET    | `/v1/disk/resources`            | `tests/test_get.py`           |
| PUT    | `/v1/disk/resources`            | `tests/test_put.py`           |
| POST   | `/v1/disk/resources/copy`       | `tests/test_post.py`          |
| DELETE | `/v1/disk/resources`            | `tests/test_delete.py`        |

## Быстрый старт

### 1. Получить OAuth-токен в Полигоне

1. Откройте [Полигон Яндекс.Диска](https://yandex.ru/dev/disk/poligon/).
2. Авторизуйтесь тестовым аккаунтом Полигона (не используйте личный Яндекс ID).
3. Скопируйте OAuth-токен из интерфейса Полигона.

### 2. Настроить окружение

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env   # Linux / macOS
```

Откройте `.env` и вставьте токен:

```
YANDEX_DISK_TOKEN=ваш_токен_из_полигона
```

### 3. Запустить тесты

```bash
pytest -v
```

## Структура проекта

```
yandex_disk/
├── api/
│   ├── __init__.py
│   └── disk_client.py      # HTTP-клиент API
├── tests/
│   ├── conftest.py         # фикстуры pytest
│   ├── test_get.py
│   ├── test_put.py
│   ├── test_post.py
│   └── test_delete.py
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Документация API

- [Обзор REST API](https://yandex.ru/dev/disk/rest/)
- [Справочник методов](https://yandex.ru/dev/disk/api/concepts/about-docpage/)
- [Полигон для отладки запросов](https://yandex.ru/dev/disk/poligon/)

## Публикация на GitHub

```bash
git init
git add .
git commit -m "Add Yandex Disk API autotests"
git remote add origin https://github.com/<username>/yandex-disk-tests.git
git push -u origin main
```

Файл `.env` с токеном в репозиторий не попадает (см. `.gitignore`).
