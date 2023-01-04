import sys
sys.path.insert(0, ".../db")

from db import get_db
g, c = get_db()

class INDE_Comunes:

    gid_provincia = 0

    def __init__(self):
        ''

    def get_INDE_comunes_by_provincia(self):
        global c

        c.execute("""
            SELECT gid_comune, gdescripcion FROM INDE_Comunes WHERE gid_provincia = %s 
            ORDER BY gdescripcion ASC
            """,
            (self.gid_provincia, )
        )

        return c.fetchall()