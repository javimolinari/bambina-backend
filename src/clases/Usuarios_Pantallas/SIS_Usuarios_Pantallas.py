from db import get_db

class SIS_Usuarios_Pantallas:

    gid_usuario = 0

    def __init__(self):
        ''
      
    def get_usuarios_pantallas(self):
        g, c = get_db()

        c.execute("""
            SELECT * FROM FVISTA_Usuarios_Pantallas
            WHERE gid_usuario = %s """, (self.gid_usuario, ))

        return c.fetchall()
   