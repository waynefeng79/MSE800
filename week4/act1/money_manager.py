from database import create_connection
import sqlite3

def add_user(name, email, address, phone):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, address, phone) VALUES (?, ?, ?, ?)", (name, email, address, phone))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")

def open_account(name, currency, open_date):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO accounts (name, currency, balance, open_date) VALUES (?, ?, ?, ?)", (name, currency, 0, open_date))
        conn.commit()
        new_account_id = cursor.lastrowid
        print(" Account opened successfully.")
    except sqlite3.IntegrityError:
        print(" Account open failed.")
        new_account_id = -1
    conn.close()
    return new_account_id

def bind_account(user_id, account_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO joint_accounts (user_id, account_id) VALUES (?, ?)", (user_id, account_id))
        conn.commit()
        print(" Account bound successfully.")
    except sqlite3.IntegrityError:
        print(" Account bound failed.")
    conn.close()

def view_accounts():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT joint_accounts.user_id, accounts.id, accounts.name, accounts.currency,
                      accounts.balance, accounts.open_date FROM accounts
                      INNER JOIN joint_accounts ON joint_accounts.account_id = accounts.id
                   """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_account(account_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM joint_accounts WHERE account_id = ?", (account_id,))
    cursor.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
    conn.commit()
    conn.close()
    print("🗑️ Account deleted.")

def add_alarm(user_id, src_currency, dst_currency, exchange_rate):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO alarm (user_id, src_currency, dst_currency, exchange_rate)
                        VALUES (?, ?, ?, ?)""", (user_id, src_currency, dst_currency, exchange_rate))
        conn.commit()
        print(" Alarm added successfully.")
    except sqlite3.IntegrityError:
        print(" Alarm add failed.")
    conn.close()

def view_alarm():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alarm")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_alarm(alarm_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alarm WHERE id = ?", (alarm_id,))
    conn.commit()
    conn.close()
    print("🗑️ Alarm deleted.")

def add_security(user_id, type, password, enabled):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO security (user_id, type, password, enabled)
                        VALUES (?, ?, ?, ?)""", (user_id, type, password, enabled))
        conn.commit()
        print(" Security added successfully.")
    except sqlite3.IntegrityError:
        print(" Security add failed.")
    conn.close()

def view_security():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM security")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_security(security_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM security WHERE id = ?", (security_id,))
    conn.commit()
    conn.close()
    print("🗑️ Security deleted.")

def add_transaction(user_id, src_account_id, dst_account_id, src_amount, dst_amount, trans_date):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO transactions (user_id, src_account_id, dst_account_id, src_amount, dst_amount, trans_date)
                        VALUES (?, ?, ?, ?, ?, ?)""",
                        (user_id, src_account_id, dst_account_id, src_amount, dst_amount, trans_date))
        conn.commit()
        print(" Transaction added successfully.")
    except sqlite3.IntegrityError:
        print(" Transaction add failed.")
    conn.close()

def view_transaction():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_transaction(transaction_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    print("🗑️ Security deleted.")