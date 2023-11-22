from backend.db.session import SessionLocal
from backend.db.data_dump import init_db


def run_db():
    db = SessionLocal()
    init_db(db)


def main():
    try:
        run_db()
    except Exception as err:
        print(err)
    else:
        print("End of initialization")


if __name__ == '__main__':
    main()
