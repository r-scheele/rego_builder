def test_get_public_and_private_repo_github(authorized_client):
    response = authorized_client.get(url="/user/repos/github")
    assert response.status_code == 200


# def test_get_data(authorized_client):
#     response = authorized_client.get(url="/data")
#     assert response.status_code == 200
