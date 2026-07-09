import sqlite3


def init_db():

    conn = sqlite3.connect("monitor.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metrics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpu REAL,
        memory REAL,
        disk REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_metrics(cpu, memory, disk):

    conn = sqlite3.connect("monitor.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO metrics(cpu,memory,disk)
        VALUES(?,?,?)
        """,
        (cpu, memory, disk)
    )

    conn.commit()
    conn.close()


def create_incident(message):

    conn = sqlite3.connect("monitor.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO incidents(message)
        VALUES(?)
        """,
        (message,)
    )

    conn.commit()
    conn.close()


def get_all_metrics():

    conn = sqlite3.connect("monitor.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM metrics
    ORDER BY id DESC
    LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_incidents():

    conn = sqlite3.connect("monitor.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM incidents
    ORDER BY id DESC
    LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


init_db()