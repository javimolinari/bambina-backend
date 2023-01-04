import sys
sys.path.insert(0, ".../db")

from db import get_db
g, c = get_db()

class INDE_Paises:
    

    def __init__(self):
        ''

    def get_INDE_paises(self):
        global c
        c.execute("""SELECT gid_pais, gdescripcion FROM INDE_Paises""")

        return c.fetchall()
   