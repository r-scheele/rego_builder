from .data import test_data


def test_write_policy(client):
    response = client.post(url="/policy/", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"status": 200, "message": "Policy created successfully"}


def test_retrieve_policy(client):
    response = client.get(url=f"/policy/{test_data['name']}")
    assert response.status_code == 200
    assert response.json() == test_data


def test_modify_policy(client):
    response = client.put(
        url=f"/policy/{test_data['name']}", json={"description": "Updated description"}
    )
    assert response.status_code == 200
    assert response.json() == {"status": 200, "message": "Updated successfully"}


def test_remove_policy(client):
    response = client.delete(url=f"/policy/{test_data['name']}")
    assert response.status_code == 200
    assert response.json() == {"status": 200, "message": "Policy deleted successfully."}
