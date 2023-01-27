from db import get_db

class Personas_busquedas:

    gid_comune = 0
    gid_persona = 0
    gid_registro = 0
    gestado = 0

    pais = ''
    provincia = ''
    comune = ''
    desde = 0
    hasta = 0
    tipodoc = ''

    registros = ''

    def __init__(self):
        ''
        # self.id_persona = 0
        # self.nombre = ''
        # self.created_by = ''

    def get_persona_busqueda_columns(self):
        g, c = get_db()

        c.execute("""
            SELECT COLUMN_NAME as colname FROM information_schema.`COLUMNS` c 
            WHERE table_name = 'FVISTA_IND_Indicesporcomune' """)

        return c.fetchall()

    def get_FVISTA_Personas_Busquedas_IndexAsociados_columns(self):
        g, c = get_db()

        c.execute("""
            SELECT COLUMN_NAME as colname FROM information_schema.`COLUMNS` c 
            WHERE table_name = 'FVISTA_Personas_Busquedas_IndexAsociados' """)

        return c.fetchall()

    def get_comunes_disponibles_by_data(self):
        g, c = get_db()

        cadena_comunes = "'" + "','".join(map(str, self.comune)) + "'"

        c.execute("""SELECT * FROM FVISTA_Personas_Busquedas_IndexDisponibles WHERE País = %s AND Provincia = %s AND 
            Comune IN (""" + cadena_comunes + """) AND Desde >= %s AND Hasta <= %s AND `Tipo documento` = %s 
            AND gid_comune NOT IN (SELECT gid_index FROM Personas_busquedas pb WHERE gid_persona = %s AND activo = 1) 
            ORDER BY País, Provincia, Comune, Desde
            """,
            (self.pais, self.provincia, self.desde, self.hasta, self.tipodoc, self.gid_persona, )
        )

        return c.fetchall()

    def get_FVISTA_Personas_Busquedas_IndexAsociados(self):
        g, c = get_db()

        c.execute("""SELECT * FROM FVISTA_Personas_Busquedas_IndexAsociados WHERE gid_persona = %s
            ORDER BY País, Provincia, Comune, Año, Parte
            """,
            (self.gid_persona, )
        )

        return c.fetchall()

    def insert_multiples_indices(self):
        g, c = get_db()

        for multi in self.comune:
            c.execute(""" 
                INSERT INTO Personas_busquedas (gid_persona, gid_index, gestado, created_by) VALUES 
                (%s, %s, %s, %s)
            """, (self.gid_persona, multi, self.gestado, 'jmolinari') )

        g.commit()

    def delete_multiples_indices(self):
        g, c = get_db()

        for multi in self.comune:
            c.execute("DELETE FROM Personas_busquedas WHERE gid_index = '%s'", (multi, ))

        g.commit()  

    def get_FVISTA_Personas_Busquedas_Objetivos(self):
        g, c = get_db()

        c.execute("""
            SELECT * FROM FVISTA_Personas_Busquedas_Objetivos 
            WHERE gid_persona = %s """, (self.gid_persona, ))

        return c.fetchone()

    def personas_busquedas_update_multi_estado_by_id(self):
        g, c = get_db()

        for r in self.registros:
            c.execute("UPDATE Personas_Busquedas_Indices SET gestado = %s WHERE gid_registro = %s ", 
                ( r[1], r[0] ))

        g.commit()




        
