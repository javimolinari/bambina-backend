from db import get_db
g, c = get_db()

class Personas:

    gid_persona = 0
    gnombre = ''
    created_by = ''

    def __init__(self):
        ''
        # self.id_persona = 0
        # self.nombre = ''
        # self.created_by = ''

    def get_personas(self):
        global c
        c.execute("SELECT * FROM FVISTA_Personas")

        return c.fetchall()

    def get_persona_by_name(self):
        global g, c

        c.execute(
            "SELECT * FROM FVISTA_Personas WHERE Nombre LIKE CONCAT ('%', %s, '%')", 
            (self.gnombre, )
        )

        return c.fetchall()

    def create_persona(self):
        global g, c
        c.execute (
            "INSERT INTO Personas (gnombre, created_by) values (%s, %s)", 
            (self.gnombre, self.created_by, )
        )
        
        id = c.lastrowid
        g.commit()

        return id
        

    def update_persona_by_id(self):
        global g, c
        c.execute (
            "UPDATE Personas SET gnombre = %s WHERE gid_persona = %s", 
            (self.gnombre, self.gid_persona, )
        )
        
        g.commit()

    def delete_persona_by_id(self):
        global g, c
        c.execute (
            "UPDATE Personas SET activo = 0 WHERE gid_persona = %s", 
            (self.gid_persona, )
        )
        
        g.commit()


