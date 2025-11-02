from ..database import get_conn

def create_table():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
            amount REAL CHECK(amount > 0) NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def get_all():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM transactions ORDER BY date DESC").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_by_id(id):
    conn = get_conn()
    row = conn.execute("SELECT * FROM transactions WHERE id = ?", (id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def create(transaction):
    conn = get_conn()
    conn.execute("""
        INSERT INTO transactions (title, category, type, amount, date)
        VALUES (?, ?, ?, ?, ?)
    """, (transaction["title"], transaction["category"], transaction["type"],
          transaction["amount"], transaction["date"]))
    conn.commit()
    conn.close()


def update(id, transaction):
    conn = get_conn()
    conn.execute("""
        UPDATE transactions SET title=?, category=?, type=?, amount=?, date=? WHERE id=?
    """, (transaction["title"], transaction["category"], transaction["type"],
          transaction["amount"], transaction["date"], id))
    conn.commit()
    conn.close()


def delete(id):
    conn = get_conn()
    conn.execute("DELETE FROM transactions WHERE id = ?", (id,))
    conn.commit()
    conn.close()