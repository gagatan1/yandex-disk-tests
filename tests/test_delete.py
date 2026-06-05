def test_delete_folder_success(disk_client, test_folder_name):
    """DELETE /v1/disk/resources — удаление папки."""
    create_response = disk_client.create_folder(path=test_folder_name)
    assert create_response.status_code == 201

    delete_response = disk_client.delete_resource(path=test_folder_name, permanently=True)
    assert delete_response.status_code in (202, 204)

    meta_response = disk_client.get_resource_meta(path=test_folder_name)
    assert meta_response.status_code == 404
