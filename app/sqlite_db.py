import sqlite3

from env_helper import config


def get_connection():
    conn = sqlite3.connect(config.TELEGRAM_CHAT_HISTORY_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def clear_all_chats():
    conn = sqlite3.connect(config.TELEGRAM_CHAT_HISTORY_DB_PATH)
    conn.execute("DELETE FROM messages")
    conn.commit()


def get_chat_history(user_id: str, limit: int = 100):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT role, content,user_id
        FROM messages
        WHERE user_id != ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (user_id, limit)
    ).fetchall()

    conn.close()

    # convert newest -> oldest into oldest -> newest
    rows = rows[::-1]

    history = []

    for r in rows:
        role = r["role"]
        content = r["content"]

        if role == "User":
            history.append(f"{r['user_id']}: {content}")
        else:
            history.append(f"assistant: {content}")
            history.append("")  # blank line between messages


    return "\n".join(history)