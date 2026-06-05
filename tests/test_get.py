from api.disk_client import YandexDiskClient


def test_get_disk_info_success(disk_client):
    """GET /v1/disk — успешное получение информации о Диске."""
    response = disk_client.get_disk_info()

    assert response.status_code == 200
    data = response.json()
    assert "total_space" in data
    assert "used_space" in data
    assert "system_folders" in data


def test_get_resource_meta_success(disk_client, created_folder, test_folder_name):
    """GET /v1/disk/resources — метаинформация о созданной папке."""
    response = disk_client.get_resource_meta(path=test_folder_name)

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_folder_name
    assert data["type"] == "dir"


def test_get_disk_info_unauthorized():
    """GET /v1/disk — запрос с невалидным токеном."""
    bad_client = YandexDiskClient(token="invalid_oauth_token")
    response = bad_client.get_disk_info()

    assert response.status_code == 401
    assert response.json()["error"] == "UnauthorizedError"
