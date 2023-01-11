import sys

from datetime import datetime
sys.path.insert(0, "db")

from db import get_db

g, c = get_db()

def algo():
    c.execute("""
    SELECT * FROM Personas""")

    print(c.fetchall())

algo()

# if fecha1 < fecha2:
#     print("ok")
#     exit()

# print("No")