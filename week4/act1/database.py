import sqlite3

def create_connection():
    conn = sqlite3.connect("money.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            address TEXT,
            phone TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            currency TEXT NOT NULL,
            balance REAL,
            open_date TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS joint_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            account_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (account_id) REFERENCES accounts (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alarm (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            src_currency TEXT NOT NULL,
            dst_currency TEXT NOT NULL,
            exchange_rate REAL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS security (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT NOT NULL,
            password TEXT NOT NULL,
            enabled INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            src_account_id INTEGER,
            dst_account_id INTEGER,
            src_amount TEXT NOT NULL,
            dst_amount TEXT NOT NULL,
            trans_date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (src_account_id) REFERENCES accounts (id),
            FOREIGN KEY (dst_account_id) REFERENCES accounts (id)
        )
    ''')

    conn.commit()
    conn.close()
