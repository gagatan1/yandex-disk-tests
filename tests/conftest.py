import os
import uuid

import pytest
from dotenv import load_dotenv

from api.disk_client import YandexDiskClient

load_dotenv()


@pytest.fixture(scope="session")
def token():
    api_token = os.getenv("YANDEX_DISK_TOKEN")
    if not api_token:
        pytest.fail(
            "Переменная YANDEX_DISK_TOKEN не задана. "
            "Скопируйте .env.example в .env и укажите OAuth-токен из Полигона."
        )
    return api_token


@pytest.fixture(scope="session")
def disk_client(token):
    return YandexDiskClient(token=token)


@pytest.fixture()
def test_folder_name():
    return f"pytest_{uuid.uuid4().hex[:8]}"


@pytest.fixture()
def test_folder_copy_name(test_folder_name):
    return f"{test_folder_name}_copy"


@pytest.fixture()
def created_folder(disk_client, test_folder_name):
    """Создаёт временную папку перед тестом и удаляет после."""
    response = disk_client.create_folder(path=test_folder_name)
    assert response.status_code == 201, response.text
    yield test_folder_name
    disk_client.delete_resource(path=test_folder_name, permanently=True)


@pytest.fixture()
def created_folder_with_copy(disk_client, created_folder, test_folder_copy_name):
    """Папка и её копия; обе удаляются после теста."""
    yield created_folder, test_folder_copy_name
    disk_client.delete_resource(path=test_folder_copy_name, permanently=True)
