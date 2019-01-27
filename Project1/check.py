import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")



engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
 f = open("books.csv")
 reader = csv.reader(f)

 rows = db.execute("SELECT * FROM books")

 for isbn, title, author, year in rows:
   print(f"{isbn}")


if __name__ == "__main__":
  main()