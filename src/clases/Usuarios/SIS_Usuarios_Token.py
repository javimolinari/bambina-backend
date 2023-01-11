from db import get_db

class SIS_Usuarios_Token:

    gid_token = 0
    gid_usuario = 0
    gtoken = ''
    gfechaexpiracion = ''

    def __init__(self):
        ''
      
    def get_usuario_token_by_idusuario(self):
        g, c = get_db()

        c.execute("""
            SELECT * FROM SIS_Usuarios_Token
            WHERE gid_usuario = %s""", (self.gid_usuario, ))

        return c.fetchone()

    def get_usuario_token_by_token(self):
        
        g, c = get_db()

        c.execute("""
            SELECT * FROM SIS_Usuarios_Token
            WHERE gtoken = %s""", (self.gtoken, ))

        return c.fetchone()

    def del_usuario_token(self):
        g, c = get_db()

        c.execute("""
            DELETE FROM SIS_Usuarios_Token
            WHERE gid_token = %s""", (self.gid_token, ))

        g.commit()


    def cre_usuario_token(self):
        g, c = get_db()

        c.execute("""
            INSERT INTO SIS_Usuarios_Token (gid_usuario, gtoken, gfechaexpiracion)
            VALUE (%s, %s, %s) """, (self.gid_usuario, self.gtoken, self.gfechaexpiracion ))
        
        g.commit()

   