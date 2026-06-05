def test_post_copy_folder_success(disk_client, created_folder, test_folder_copy_name):
    """POST /v1/disk/resources/copy — копирование папки."""
    response = disk_client.copy_resource(
        from_path=created_folder,
        to_path=test_folder_copy_name,
    )

    assert response.status_code == 201
    body = response.json()
    assert "href" in body
    assert body["method"] == "GET"

    meta = disk_client.get_resource_meta(path=test_folder_copy_name)
    assert meta.status_code == 200
    assert meta.json()["name"] == test_folder_copy_name

    disk_client.delete_resource(path=test_folder_copy_name, permanently=True)
