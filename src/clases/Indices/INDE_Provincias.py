import sys
sys.path.insert(0, ".../db")

from db import get_db
g, c = get_db()

class INDE_Provincias:

    gid_pais = 0

    def __init__(self):
        ''

    def get_INDE_provincias_by_pais(self):
        global c

        c.execute("""
            SELECT gid_provincia, gdescripcion FROM INDE_Provincias WHERE gid_pais = %s 
            ORDER BY gdescripcion ASC
            """,
            (self.gid_pais, )
        )

        return c.fetchall()

   