from db import get_db

class INDE_TiposDocumento:

    def __init__(self):
        ''

    def get_INDE_TiposDocumento(self):
        g, c = get_db()
        
        c.execute("""SELECT gdescripcion FROM INDE_TiposDocumento""")

        return c.fetchall()
   