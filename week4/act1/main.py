from database import create_table
from money_manager import *
from datetime import datetime

types = ["User", "Account", "Alarm", "Security", "Transaction"]

def menu_type():
    print(f"1. {types[0]}")
    print(f"2. {types[1]}")
    print(f"3. {types[2]}")
    print(f"4. {types[3]}")
    print(f"5. {types[4]}")
    print(f"6. Exit")

def menu(name):
    print(f"\n==== {name} Manager ====")
    print(f"1. Add {name}")
    print(f"2. View All {name}")
    print(f"3. Delete {name} by ID")
    if name == types[0]:
        print(f"4. Search {name} by Name")
        menu_users()
    elif name == types[1]:
        menu_accounts()
    elif name == types[2]:
        menu_alarm()
    elif name == types[3]:
        menu_security()
    elif name == types[4]:
        menu_transactions()

def menu_users():
    while True:
        choice = input("Select an option (1-4): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            phone = input("Enter phone: ")
            add_user(name, email, address, phone)
            break
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
            break
        elif choice == '3':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
            break
        elif choice == '4':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
            break
        else:
            print("Invalid choice, try again.")

def menu_accounts():
    while True:
        choice = input("Select an option (1-3): ")
        if choice == '1':
            name = input("Enter name: ")
            currency = input("Enter currency: ")
            open_date = datetime.now()
            account_id = open_account(name, currency, open_date)
            user_id = input("Enter user ID associating with this account: ")
            bind_account(user_id, account_id)
            break
        elif choice == '2':
            accounts = view_accounts()
            for account in accounts:
                print(account)
            break
        elif choice == '3':
            account_id = int(input("Enter account ID to delete: "))
            delete_account(account_id)
            break
        else:
            print("Invalid choice, try again.")

def menu_alarm():
    while True:
        choice = input("Select an option (1-3): ")
        if choice == '1':
            user_id = input("Enter User ID: ")
            src_currency = input("Enter source currency: ")
            dst_currency = input("Enter destination currency: ")
            exchange_rate = float(input("Enter exchange rate: "))
            add_alarm(user_id, src_currency, dst_currency, exchange_rate)
            break
        elif choice == '2':
            alarms = view_alarm()
            for alarm in alarms:
                print(alarm)
            break
        elif choice == '3':
            alarm_id = int(input("Enter alarm ID to delete: "))
            delete_alarm(alarm_id)
            break
        else:
            print("Invalid choice, try again.")

def menu_security():
    while True:
        choice = input("Select an option (1-3): ")
        if choice == '1':
            user_id = input("Enter User ID: ")
            type = input("Enter security type: ")
            password = input("Enter security password: ")
            enabled = int(input("Is security enabled(1/0): "))
            add_security(user_id, type, password, enabled)
            break
        elif choice == '2':
            securities = view_security()
            for security in securities:
                print(security)
            break
        elif choice == '3':
            security_id = int(input("Enter security ID to delete: "))
            delete_security(security_id)
            break
        else:
            print("Invalid choice, try again.")

def menu_transactions():
    while True:
        choice = input("Select an option (1-3): ")
        if choice == '1':
            user_id = input("Enter User ID: ")
            src_account = input("Enter source account ID: ")
            dst_account = input("Enter destination account ID: ")
            src_amount = float(input("Enter source account amount: "))
            dst_amount = float(input("Enter destination account amount: "))
            trans_date = datetime.now()
            add_transaction(user_id, src_account, dst_account, src_amount, dst_amount, trans_date)
            break
        elif choice == '2':
            transactions = view_transaction()
            for transaction in transactions:
                print(transaction)
            break
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete_account(transaction_id)
            break
        else:
            print("Invalid choice, try again.")

def main():
    create_table()
    while True:
        menu_type()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            menu(types[0])
        elif choice == '2':
            menu(types[1])
        elif choice == '3':
            menu(types[2])
        elif choice == '4':
            menu(types[3])
        elif choice == '5':
            menu(types[4])
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
        
if __name__ == "__main__":
    main()
