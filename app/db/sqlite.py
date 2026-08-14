import sqlite_utils

DB_PATH = "incidents.db"

def get_db():
    return sqlite_utils.Database(DB_PATH)

def init_db():
    db = get_db()
    if "incidents" not in db.table_names():
        db["incidents"].create({
            "id": int,
            "title": str,
            "severity": str,
            "created_at": str
        }, pk="id")
