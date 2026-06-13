from app_session import AppSession
from database import Database

def main():
    db =Database("app.db")
    # Start the command-line workflow; session.run owns the menu loop.
    session = AppSession(db)
    session.run()

if __name__ == "__main__":
    main()
