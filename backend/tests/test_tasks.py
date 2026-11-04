
def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Learn automated testing",
            "description": "Testing FastAPI with pytest",
            "priority": "high"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Learn automated testing"
    assert data["priority"] == "high"
    assert data["completed"] is False


def test_get_tasks(client):
    client.post(
        "/tasks",
        json={
            "title": "Test retrieval",
            "description": "Retrieve tasks from PostgreSQL",
            "priority": "medium"
        }
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_nonexistent_task(client):
    response = client.get("/tasks/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_update_task(client):
    created = client.post(
        "/tasks",
        json={"title": "Old title", "priority": "low"}
    )
    task_id = created.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated title",
            "description": "Updated description",
            "priority": "high",
            "completed": True
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"
    assert response.json()["completed"] is True


def test_patch_task(client):
    created = client.post(
        "/tasks",
        json={"title": "Original title", "priority": "low"}
    )
    task_id = created.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={"completed": True}
    )

    assert response.status_code == 200
    assert response.json()["completed"] is True
    assert response.json()["title"] == "Original title"


def test_delete_task(client):
    created = client.post(
        "/tasks",
        json={"title": "Task to delete"}
    )
    task_id = created.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204

    check = client.get(f"/tasks/{task_id}")
    assert check.status_code == 404


def test_invalid_priority(client):
    response = client.post(
        "/tasks",
        json={"title": "Invalid task", "priority": "urgent"}
    )

    assert response.status_code == 422


def test_empty_title(client):
    response = client.post(
        "/tasks",
        json={"title": ""}
    )

    assert response.status_code == 422


def test_update_nonexistent_task(client):
    response = client.put(
        "/tasks/99999",
        json={
            "title": "Missing",
            "description": "",
            "priority": "medium",
            "completed": False
        }
    )

    assert response.status_code == 404


def test_delete_nonexistent_task(client):
    response = client.delete("/tasks/99999")

    assert response.status_code == 404