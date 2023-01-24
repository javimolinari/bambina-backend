from db import get_db

class SIS_Usuarios:

    gid_usuario = 0
    gid_rol = 0
    gusuario = ''
    gpassword = ''
    gtoken = ''
    gfechaexpiracion = ''
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

    def get_usuario_by_token(self):
        g, c = get_db()

        c.execute("""
            SELECT * FROM FVISTA_SIS_Usuarios
            WHERE Token = %s """, (self.gtoken, ))

        return c.fetchone()

    def update_token_by_id(self):
        g, c = get_db()

        c.execute (
            "UPDATE SIS_Usuarios SET gtoken = %s WHERE gid_usuario = %s", 
            (self.gtoken, self.gid_usuario )
        )
        
        g.commit()

    def delete_token_usuario(self):
        g, c = get_db()
        
        c.execute (
            "UPDATE SIS_Usuarios SET gtoken = '', gfechaexpiracion = NULL WHERE gid_usuario = %s", 
            (self.gid_usuario, )
        )
        
        g.commit()

   

