from db import get_db

class INDE_IndicesPorComune:

    gid_index = 0
    gpais = ''
    gprovincia = ''
    gcomune = ''
    gdesde = ''
    ghasta = ''
    gparte = ''
    gtipo = ''
    gconcatalogo = ''
    gconindice = ''
    gobservaciones = ''
    gurl = ''

    def __init__(self):
        ''

    def get_INDE_IndiciesPorComune_por_url(self):
        g, c = get_db()

        c.execute("""
            SELECT gid_index, gpais, gprovincia, gcomune, gdesde, ghasta, gparte, gtipo, gconindice, 
            gconcatalogo, gobservaciones, gurl 
            FROM INDE_IndicesPorComune WHERE gurl = %s 
            """,
            (self.gurl, )
        )

        return c.fetchone()


    def update_INDE_IndiciesPorComune_por_idindex(self):
        g, c = get_db()

        c.execute("""

            UPDATE INDE_IndicesPorComune SET gpais = %s, gprovincia = %s, 
            gcomune = %s, gdesde = %s, ghasta = %s, gparte = %s, gtipo = %s, gconindice = %s, 
            gconcatalogo = %s, gobservaciones = %s, gurl = %s 
            WHERE gid_index = %s 
            """,
            (self.gpais, self.gprovincia, self.gcomune, self.gdesde, self.ghasta, self.gparte,
             self.gtipo, self.gconindice, self.gconcatalogo, self.gobservaciones, self.gurl, self.gid_index )
        )

        g.commit()