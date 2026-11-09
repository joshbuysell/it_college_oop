from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request


def init_db(database_path: Path) -> None:
    with sqlite3.connect(database_path) as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS tasks "
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)"
        )


def export_tasks(database_path: Path, json_path: Path) -> None:
    with sqlite3.connect(database_path) as connection:
        rows = connection.execute(
            "SELECT id, title FROM tasks ORDER BY id"
        ).fetchall()
    tasks = [{"id": task_id, "title": title} for task_id, title in rows]
    json_path.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


def load_tasks(json_path: Path) -> list[dict[str, int | str]]:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("JSON має містити список завдань")
    return data


def create_app(database_path: Path, json_path: Path) -> Flask:
    app = Flask(__name__)
    app.config["DATABASE_PATH"] = database_path
    app.config["JSON_PATH"] = json_path
    init_db(database_path)

    @app.get("/tasks")
    def get_tasks():
        with sqlite3.connect(database_path) as connection:
            rows = connection.execute(
                "SELECT id, title FROM tasks ORDER BY id"
            ).fetchall()
        return jsonify([{"id": task_id, "title": title} for task_id, title in rows])

    @app.post("/tasks")
    def create_task():
        payload = request.get_json(silent=True) or {}
        title = payload.get("title")
        if not isinstance(title, str) or not title.strip():
            return jsonify({"error": "Поле title є обов'язковим"}), 400
        title = title.strip()
        with sqlite3.connect(database_path) as connection:
            cursor = connection.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
            task_id = cursor.lastrowid
        export_tasks(database_path, json_path)
        return jsonify({"id": task_id, "title": title}), 201

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id: int):
        with sqlite3.connect(database_path) as connection:
            cursor = connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            return jsonify({"error": "Завдання не знайдено"}), 404
        export_tasks(database_path, json_path)
        return jsonify({"deleted_id": task_id}), 200

    return app