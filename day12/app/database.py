import sqlite3

DATABASE = "tasks.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)
        conn.commit()


def db_get_all_tasks(status=None):
    with get_connection() as conn:

        if status == "pending":
            rows = conn.execute(
                "SELECT * FROM tasks WHERE completed = 0"
            ).fetchall()

        elif status == "completed":
            rows = conn.execute(
                "SELECT * FROM tasks WHERE completed = 1"
            ).fetchall()

        else:
            rows = conn.execute(
                "SELECT * FROM tasks"
            ).fetchall()

        return [
            {
                "id": row["id"],
                "title": row["title"],
                "completed": bool(row["completed"])
            }
            for row in rows
        ]


def db_get_task(task_id):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        if not row:
            return None

        return {
            "id": row["id"],
            "title": row["title"],
            "completed": bool(row["completed"])
        }


def db_create_task(data):
    with get_connection() as conn:

        cursor = conn.execute(
            """
            INSERT INTO tasks(title, completed)
            VALUES (?, ?)
            """,
            (data.title, 0)
        )

        conn.commit()

        new_id = cursor.lastrowid

        return db_get_task(new_id)


def db_update_task(task_id, data):
    with get_connection() as conn:

        cursor = conn.execute(
            """
            UPDATE tasks
            SET title = ?, completed = ?
            WHERE id = ?
            """,
            (data.title, int(data.completed), task_id)
        )

        conn.commit()

        if cursor.rowcount == 0:
            return None

        return db_get_task(task_id)


def db_delete_task(task_id):
    with get_connection() as conn:

        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()

        return cursor.rowcount > 0


def db_complete_task(task_id):
    with get_connection() as conn:

        cursor = conn.execute(
            """
            UPDATE tasks
            SET completed = 1
            WHERE id = ?
            """,
            (task_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            return None

        return db_get_task(task_id)