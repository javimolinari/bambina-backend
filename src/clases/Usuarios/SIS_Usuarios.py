from db import get_db

class SIS_Usuarios:

    gid_usuario = 0
    gid_rol = 0
    gusuario = ''
    gpassword = ''
    gnombre = ''
    created_by = ''

    def __init__(self):
        ''
      
    def get_usuario(self):
        g, c = get_db()

        c.execute("""
            SELECT * FROM FVISTA_SIS_Usuarios
            WHERE Usuario = %s AND Password = %s""", (self.gusuario, self.gpassword ))

        return c.fetchone()
   

