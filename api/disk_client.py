import requests


class YandexDiskClient:
    """HTTP-клиент для REST API Яндекс.Диска (https://cloud-api.yandex.net)."""

    def __init__(self, token: str, base_url: str = "https://cloud-api.yandex.net/v1/disk"):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"OAuth {token}",
            "Content-Type": "application/json",
        }

    def get_disk_info(self) -> requests.Response:
        """GET /v1/disk — данные о Диске пользователя."""
        return requests.get(self.base_url, headers=self.headers)

    def get_resource_meta(self, path: str) -> requests.Response:
        """GET /v1/disk/resources — метаинформация о файле или папке."""
        url = f"{self.base_url}/resources"
        return requests.get(url, headers=self.headers, params={"path": path})

    def create_folder(self, path: str) -> requests.Response:
        """PUT /v1/disk/resources — создать папку."""
        url = f"{self.base_url}/resources"
        return requests.put(url, headers=self.headers, params={"path": path})

    def copy_resource(self, from_path: str, to_path: str, overwrite: bool = False) -> requests.Response:
        """POST /v1/disk/resources/copy — скопировать файл или папку."""
        url = f"{self.base_url}/resources/copy"
        params = {
            "from": from_path,
            "path": to_path,
            "overwrite": str(overwrite).lower(),
        }
        return requests.post(url, headers=self.headers, params=params)

    def delete_resource(self, path: str, permanently: bool = True) -> requests.Response:
        """DELETE /v1/disk/resources — удалить файл или папку."""
        url = f"{self.base_url}/resources"
        params = {
            "path": path,
            "permanently": str(permanently).lower(),
        }
        return requests.delete(url, headers=self.headers, params=params)
