from db import get_db

class INDE_Paises:

    def __init__(self):
        ''

    def get_INDE_paises(self):
        g, c = get_db()
        
        c.execute("""SELECT gid_pais, gdescripcion FROM INDE_Paises""")

        return c.fetchall()
   