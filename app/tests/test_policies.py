from .data import test_request_object


def test_write_policy(authorized_client):

    response = authorized_client.post(url="/policies/", json=test_request_object)
    assert response.status_code == 200
    assert response.json() == {"status": 200, "message": "Policy created successfully"}


def test_retrieve_policy(authorized_client):
    response = authorized_client.get(url=f"/policies/{test_request_object['name']}")
    assert response.status_code == 200


def test_modify_policy(authorized_client):
    response = authorized_client.put(
        url=f"/policies/{test_request_object['name']}",
        json=test_request_object,
    )

    assert response.status_code == 200
    assert response.json() == {"status": 200, "message": "Updated successfully"}


def test_remove_policy(authorized_client):
    response = authorized_client.delete(
        url=f"/policies/{test_request_object['name']}?repo_url={test_request_object['repo_url']}"
    )
    assert response.status_code == 200
    assert response.json() == {"status": 200, "message": "Policy deleted successfully."}


def test_list_policies(authorized_client):
    response = authorized_client.get(url="/policies/")
    assert response.status_code == 200
