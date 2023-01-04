from db import get_db
g, c = get_db()

class SIS_Usuarios_Token:

    gid_usuario = 0
    gtoken = ''
    gfechaexpiracion = ''

    def __init__(self):
        ''
      
    def get_usuario_token_by_idusuario(self):
        global c
        c.execute("""
            SELECT * FROM SIS_Usuarios_Token
            WHERE gid_usuario = %s""", (self.gid_usuario, ))

        return c.fetchone()

    def get_usuario_token_by_token(self):
        global c
        c.execute("""
            SELECT * FROM SIS_Usuarios_Token
            WHERE gtoken = %s""", (self.gtoken, ))

        return c.fetchone()

    def del_usuario_token(self):
        global c
        c.execute("""
            DELETE FROM SIS_Usuarios_Token
            WHERE gtoken = %s""", (self.gtoken, ))

        g.commit()


    def cre_usuario_token(self):
        global c
        c.execute("""
            INSERT INTO SIS_Usuarios_Token (gid_usuario, gtoken, gfechaexpiracion)
            VALUE (%s, %s, %s) """, (self.gid_usuario, self.gtoken, self.gfechaexpiracion ))
        
        g.commit()

   