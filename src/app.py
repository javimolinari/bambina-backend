import sys
sys.path.insert(0, "db")
sys.path.append('/clases')

from flask import Flask, request, jsonify, session
from flask_cors import CORS
import functools

import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Gskdjanasjdl'
db.init_app(app)

CORS(app)


def token_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwars):
        if session.get('token') is None:
            return jsonify('Expired')

        return view(**kwars)

    return wrapped_view


@app.route('/api/pepe', methods=['GET'])
def pruebas():
    from clases.Personas.Personas import Personas
    p = Personas()

    print (p.get_personas())


    return jsonify("SERVER CONNECTED")

### RUTAS DE PERSONAS
@app.route('/api/get_personas', methods=['GET'])
def get_personas():
    from clases.Personas.Personas import Personas
    p = Personas()

    return jsonify(p.get_personas())
 
@app.route('/api/get_persona_by_name', methods=['GET'])
def get_persona_by_name():
    from clases.Personas.Personas import Personas
    Personas = Personas()

    r = request.args
    Personas.gnombre = r.get('gnombre')
    
    return jsonify(Personas.get_persona_by_name())

@app.route('/api/create_persona', methods=['POST'])
def create_persona():
    from clases.Personas.Personas import Personas
    p = Personas()

    r = request.json
    p.gnombre = r['nombre']
    p.created_by = r['created_by']
    
    return jsonify(p.create_persona())

@app.route('/api/update_persona_by_id', methods=['PUT'])
def update_persona_by_id():
    from clases.Personas.Personas import Personas
    p = Personas()

    r = request.json
    p.gid_persona = r['id_persona']
    p.gnombre = r['nombre']
    p.update_persona_by_id()
    
    return jsonify(p.get_personas())

@app.route('/api/delete_persona_by_id', methods=['DELETE'])
def delete_persona_by_id():
    from clases.Personas import Personas
    p = Personas()

    r = request.json
    p.gid_persona = r['id_persona']
    p.delete_persona_by_id()
    
    return jsonify(p.get_personas())


### RUTAS DE INDE_Paises
@app.route('/api/get_INDE_Paises', methods=['GET'])
@token_required
def get_INDE_Paises():
    try:
        from clases.Indices.INDE_Paises import INDE_Paises
        return jsonify(INDE_Paises().get_INDE_paises())
    
    except Exception as e:
        return jsonify("Entre en error en get_INDE_Paises", e)

###RUTAS DE INDE_Provincias
@app.route('/api/get_INDE_Provincias_by_pais', methods=['GET'])
def get_INDE_Provincias_by_pais():
    try:
        from clases.Indices.INDE_Provincias import INDE_Provincias

        INDE_Provincias = INDE_Provincias()
        INDE_Provincias.gid_pais = request.json

        return jsonify(INDE_Provincias.get_INDE_provincias_by_pais())
    
    except Exception as e:
        return jsonify("Entre en error en get_INDE_Provincias_by_pais")

###RUTAS DE INDE_Comunes
@app.route('/api/get_INDE_comunes_by_provincia', methods=['GET'])
def get_INDE_comunes_by_provincia():
    try:
        from clases.Indices.INDE_Comunes import INDE_Comunes

        INDE_Comunes = INDE_Comunes()
        INDE_Comunes.gid_provincia = request.json

        return jsonify(INDE_Comunes.get_INDE_comunes_by_provincia())
    
    except Exception as e:
        return jsonify("Entre en error en get_INDE_comunes_by_provincia", e)

###RUTAS DE INDE_TiposDocumentos
@app.route('/api/get_INDE_TiposDocumentos', methods=['GET'])
def get_INDE_TiposDocumento():
    try:
        from clases.Indices.INDE_TiposDocumento import INDE_TiposDocumento
        INDE_TiposDocumento = INDE_TiposDocumento()

        return jsonify(INDE_TiposDocumento.get_INDE_TiposDocumento())

    except Exception as e:
        return jsonify("Entre en error en get_INDE_TiposDocumento")



###RUTAS DE PERSONAS_BUSQUEDAS
@app.route('/api/get_persona_busqueda_columns', methods=['GET'])
def get_persona_busqueda_columns():

    try:
        from clases.personas_busquedas.Personas_busquedas import Personas_busquedas
        return jsonify(Personas_busquedas().get_persona_busqueda_columns())

    except Exception as e:
        return jsonify("Entre en el error  get_persona_busqueda_columns")

@app.route('/api/get_FVISTA_Personas_Busquedas_IndexAsociados_columns', methods=['GET'])
def get_FVISTA_Personas_Busquedas_IndexAsociados_columns():
    try:
        from clases.personas_busquedas.Personas_busquedas import Personas_busquedas
        return jsonify(Personas_busquedas().get_FVISTA_Personas_Busquedas_IndexAsociados_columns())

    except Exception as e:
        return jsonify("Entre en el error get_FVISTA_Personas_Busquedas_IndexAsociados_columns")

@app.route('/api/get_comunes_disponibles_by_data', methods=['GET'])
def get_comunes_disponibles_by_data():
    try:

        from clases.personas_busquedas.Personas_busquedas import Personas_busquedas

        r = request.json
        Personas_busquedas = Personas_busquedas()
        Personas_busquedas.gid_persona = r['gid_persona']
        Personas_busquedas.pais = r['pais']
        Personas_busquedas.provincia = r['provincia']
        Personas_busquedas.comune = r['comunes']
        Personas_busquedas.desde = r['desde']
        Personas_busquedas.hasta = r['hasta']
        Personas_busquedas.tipodoc = r['tipo']

        return jsonify(Personas_busquedas.get_comunes_disponibles_by_data())
    
    except Exception as e:
        return jsonify("Entre en el error en get_comunes_disponibles_by_data", e);

@app.route('/api/get_FVISTA_Personas_Busquedas_IndexAsociados', methods=['GET'])
def get_FVISTA_Personas_Busquedas_IndexAsociados():
    try:
        from clases.personas_busquedas.Personas_busquedas import Personas_busquedas
        r = request.args

        Personas_busquedas = Personas_busquedas()
        Personas_busquedas.gid_persona = r.get('gid_persona')

        return jsonify(Personas_busquedas.get_FVISTA_Personas_Busquedas_IndexAsociados())
    except Exception as e:
        return jsonify("Entre en error en get_indices_asociados_by_idpersona", e)

@app.route('/api/insert_multiples_indices', methods=['POST'])
def insert_multiples_indices():
    try:
        from clases.personas_busquedas.Personas_busquedas import Personas_busquedas

        r = request.json

        Personas_busquedas = Personas_busquedas()
        Personas_busquedas.comune = r['nuevos']
        Personas_busquedas.gid_persona = r['gid_persona']
        Personas_busquedas.gestado = 0

        Personas_busquedas.insert_multiples_indices()

        return jsonify("Se han ingresado los registrados asociados correctamente")

    except Exception as e:
        return jsonify("Entre en error en get_indices_asociados_by_idpersona", e)

@app.route('/api/delete_multiples_indices', methods=['POST'])
def delete_multiples_indices():
    try:
        from clases.personas_busquedas.Personas_busquedas import Personas_busquedas

        r = request.json

        Personas_busquedas = Personas_busquedas()
        Personas_busquedas.comune = r['nuevos']

        Personas_busquedas.delete_multiples_indices()

        return jsonify("Se ha eliminado los registrados liberados correctamente")

    except Exception as e:
        return jsonify("Entre en error en get_indices_asociados_by_idpersona", e)


@app.route('/api/get_FVISTA_Personas_Busquedas_Objetivos', methods=['GET'])
def get_FVISTA_Personas_Busquedas_Objetivos():
    try:
        from clases.personas_busquedas.Personas_busquedas import Personas_busquedas
        r = request.args

        Personas_busquedas = Personas_busquedas()
        Personas_busquedas.gid_persona = r.get('gid_persona')

        return jsonify( Personas_busquedas.get_FVISTA_Personas_Busquedas_Objetivos())

    except Exception as e:
        return jsonify("Entre en error en get_indices_asociados_by_idpersona", e)

### RUTAS SIS_USUARIOS
@app.route('/api/get_usuario', methods=['POST'])
def get_usuario():
    try:
        from clases.Usuarios.SIS_Usuarios import SIS_Usuarios
        from clases.Usuarios.SIS_Usuarios_Token import SIS_Usuarios_Token

        r = request.json

        SIS_Usuarios = SIS_Usuarios()
        SIS_Usuarios.gusuario = r['gusuario']
        SIS_Usuarios.gpassword = r['gpassword']
        
        usu = SIS_Usuarios.get_usuario()

        if not usu:
            return "El usuario o la contraseña son incorrectos"

        SIS_Usuarios_Token = SIS_Usuarios_Token()
        SIS_Usuarios_Token.gid_usuario = usu['gid_usuario']

        token = SIS_Usuarios_Token.get_usuario_token_by_idusuario()

        if not token:
            from clases.Usuarios.Code_generator import code_generator, add_days
           
            token, date = code_generator()

            if r['gmantener'] == 'si':
                tp = add_days(date, 14)
            else:
                tp = add_days(date, 1)

            SIS_Usuarios_Token.gid_usuario = usu['gid_usuario']
            SIS_Usuarios_Token.gtoken = token
            SIS_Usuarios_Token.gfechaexpiracion = tp
            SIS_Usuarios_Token.cre_usuario_token()

            session.clear()
            session['token'] = token

        return jsonify(token)

    except Exception as e:
        return jsonify("Entre en error en get_usuario", e)

@app.route('/api/notExpired', methods=['POST'])
def get_usuario_token_by_token():
    try:
        from clases.Usuarios.SIS_Usuarios_Token import SIS_Usuarios_Token
        from datetime import datetime

        r = request.json

        SIS_Usuarios_Token = SIS_Usuarios_Token()
        SIS_Usuarios_Token.gtoken = r[2:] #saco los primeros dos caracteres

        datos = SIS_Usuarios_Token.get_usuario_token_by_token()

        if not datos:
            return jsonify ("close")

        if datos['gfechaexpiracion'] < datetime.now():
            SIS_Usuarios_Token.gid_token = datos['gid_token']
            SIS_Usuarios_Token.del_usuario_token()

            return jsonify ("close")
        
        return jsonify ("ok")

    except Exception as e:
        return jsonify("Entre en error en get_usuario_token_by_token", e)


if __name__=='__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.run(debug=True)