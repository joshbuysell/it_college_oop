import json
import sqlite3

import pytest

from app import create_app, export_tasks, init_db, load_tasks


@pytest.fixture
def resources(tmp_path):
    database_path = tmp_path / "tasks.db"
    json_path = tmp_path / "tasks.json"
    app = create_app(database_path, json_path)
    app.config.update(TESTING=True)
    return app, database_path, json_path


def test_init_db_creates_tasks_table(tmp_path):
    database_path = tmp_path / "tasks.db"
    init_db(database_path)
    with sqlite3.connect(database_path) as connection:
        table = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'tasks'"
        ).fetchone()
    assert table == ("tasks",)


def test_create_task_persists_in_database_and_json(resources):
    app, database_path, json_path = resources
    response = app.test_client().post("/tasks", json={"title": "Вивчити pytest"})

    assert response.status_code == 201
    assert response.get_json()["title"] == "Вивчити pytest"
    with sqlite3.connect(database_path) as connection:
        row = connection.execute("SELECT id, title FROM tasks").fetchone()
    assert row == (1, "Вивчити pytest")
    assert load_tasks(json_path) == [{"id": 1, "title": "Вивчити pytest"}]


def test_get_tasks_returns_empty_list(resources):
    app, _, _ = resources
    response = app.test_client().get("/tasks")

    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task_without_title_returns_bad_request(resources):
    app, _, _ = resources
    response = app.test_client().post("/tasks", json={})

    assert response.status_code == 400
    assert "title" in response.get_json()["error"]


def test_create_two_tasks_preserves_database_order(resources):
    app, database_path, _ = resources
    client = app.test_client()
    client.post("/tasks", json={"title": "Перше завдання"})
    client.post("/tasks", json={"title": "Друге завдання"})

    with sqlite3.connect(database_path) as connection:
        rows = connection.execute("SELECT title FROM tasks ORDER BY id").fetchall()
    assert rows == [("Перше завдання",), ("Друге завдання",)]


def test_export_empty_database_creates_empty_json(tmp_path):
    database_path = tmp_path / "tasks.db"
    json_path = tmp_path / "tasks.json"
    init_db(database_path)

    export_tasks(database_path, json_path)

    assert load_tasks(json_path) == []


def test_load_tasks_rejects_corrupted_json(tmp_path):
    json_path = tmp_path / "broken.json"
    json_path.write_text("{broken json", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_tasks(json_path)


def test_delete_task_removes_database_and_json_record(resources):
    app, database_path, json_path = resources
    client = app.test_client()
    created = client.post("/tasks", json={"title": "Видалити це"}).get_json()

    response = client.delete(f"/tasks/{created['id']}")

    assert response.status_code == 200
    with sqlite3.connect(database_path) as connection:
        assert connection.execute("SELECT * FROM tasks").fetchall() == []
    assert load_tasks(json_path) == []


def test_delete_missing_task_returns_not_found(resources):
    app, _, _ = resources

    response = app.test_client().delete("/tasks/999")

    assert response.status_code == 404