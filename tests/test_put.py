def test_put_create_folder_success(disk_client, test_folder_name):
    """PUT /v1/disk/resources — создание папки."""
    response = disk_client.create_folder(path=test_folder_name)

    assert response.status_code == 201
    body = response.json()
    assert body["method"] == "GET"
    assert "href" in body

    meta = disk_client.get_resource_meta(path=test_folder_name)
    assert meta.status_code == 200
    assert meta.json()["name"] == test_folder_name

    disk_client.delete_resource(path=test_folder_name, permanently=True)


def test_put_create_folder_conflict(disk_client, created_folder, test_folder_name):
    """PUT /v1/disk/resources — повторное создание существующей папки."""
    response = disk_client.create_folder(path=test_folder_name)

    assert response.status_code == 409
    assert response.json()["error"] == "DiskPathPointsToExistentDirectoryError"
