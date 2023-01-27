import sys
sys.path.insert(0, "db")
sys.path.append('/clases')

from flask import Flask, request, jsonify, session
from flask_cors import CORS
import functools

import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Gskdjanasjdl'
app.config['JSON_SORT_KEYS'] = False

db.init_app(app)

CORS(app)

logs = {}


def token_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwars):
        if session.get('token') is None:
            return jsonify('Expired')

        return view(**kwars)

    return wrapped_view


@app.route('/api/pepe', methods=['GET'])
def pruebas():
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

@app.route('/api/personas_busquedas_update_multi_estado', methods=['PATCH'])
def personas_busquedas_update_multi_estado():
    try:
        from clases.personas_busquedas.Personas_busquedas import Personas_busquedas

        Personas_busquedas = Personas_busquedas()
        Personas_busquedas.registros = request.json['registros']

        Personas_busquedas.personas_busquedas_update_multi_estado_by_id()

        return jsonify("ok")

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
        global logs

        from clases.Usuarios.SIS_Usuarios import SIS_Usuarios
        from clases.Usuarios_Pantallas.SIS_Usuarios_Pantallas import SIS_Usuarios_Pantallas

        r = request.json

        SIS_Usuarios = SIS_Usuarios()
        SIS_Usuarios.gusuario = r['gusuario']
        SIS_Usuarios.gpassword = r['gpassword']
        
        usu = SIS_Usuarios.get_usuario()

        if not usu:
            return jsonify("El usuario o la contraseña son incorrectos")

        #Si el usuario existe, busca las pantallas permitidas del usuario
        SIS_Usuarios_Pantallas = SIS_Usuarios_Pantallas()
        SIS_Usuarios_Pantallas.gid_usuario = usu['gid_usuario']
        pantallas = SIS_Usuarios_Pantallas.get_usuarios_pantallas()
        
        numtoken = ''

        #Si no existe un token, genera uno
        if usu['Token'] == '':
            from clases.Usuarios.Code_generator import code_generator, add_days
           
            token = code_generator()

            SIS_Usuarios.gid_usuario = usu['gid_usuario']
            SIS_Usuarios.gtoken = token
            SIS_Usuarios.update_token_by_id()

            #Asigno el token nuevo generado para cargar en session
            numtoken = token

        else:
            #Asigno el token activo desde de BBDD para cargar en session
            numtoken = usu['Token']

        #Creo la nueva session del token y asocio las pantallas permitidas
        logs[numtoken] = {}
        logs[numtoken]['Token'] = numtoken
        logs[numtoken]['Pantallas'] = []

        for p in pantallas:
            logs[numtoken]['Pantallas'].append([p['Pantalla'], p['Ruta']])

      
        return jsonify(logs[numtoken])

    except Exception as e:
        return jsonify("Entre en error en get_usuario", e)

@app.route('/api/token_exists', methods=['POST'])
def token_exists():
    try:
        #Comprueba que el token se encuentre en el diccionario de logs. Si es así, retorna los datos
        #del usuario con el token solamente. Sino, crea la sesion
        if request.json in logs:
            return jsonify(logs[request.json])

        #Get de los datos del usuario por token
        from clases.Usuarios.SIS_Usuarios import SIS_Usuarios
        SIS_Usuarios = SIS_Usuarios()
        SIS_Usuarios.gtoken = request.json
        datos = SIS_Usuarios.get_usuario_by_token()

        #Si no existe, devuelve close
        if not datos:
            return jsonify ("not logged")

        #Creo la session del usuario en memoria para luego cargar los permisos
        logs[datos['Token']] = {}
        logs[datos['Token']]['Token'] = datos['Token']
        logs[datos['Token']]['Pantallas'] = []

        from clases.Usuarios_Pantallas.SIS_Usuarios_Pantallas import SIS_Usuarios_Pantallas
        SIS_Usuarios_Pantallas = SIS_Usuarios_Pantallas()
        SIS_Usuarios_Pantallas.gid_usuario = datos['gid_usuario']
        pantallas = SIS_Usuarios_Pantallas.get_usuarios_pantallas()

        for p in pantallas:
            logs[datos['Token']]['Pantallas'].append([p['Pantalla'], p['Ruta']])

        return jsonify(logs[datos['Token']])

    except Exception as e:
        return jsonify("Entre en error en get_usuario_token_by_token", e)

@app.route('/api/has_permission', methods=['POST'])
def has_permission():
    try:
        r = request.json

        #Comprueba que el token se encuentre en el diccionario de logs. Si es así, retorna los datos
        #del usuario con el token solamente. Sino, crea la sesion
        if not r['gtoken'] in logs:
            return jsonify("Not logged")

        for p in logs[r['gtoken']]['Pantallas']:
            if p[0] == r['gpantalla']:
                return jsonify('accept')
        
        return jsonify('denied')

    except Exception as e:
        return jsonify("Entre en error en get_usuario_token_by_token", e)

@app.route('/api/session', methods=['GET'])
def session():
    return jsonify(logs)

if __name__=='__main__':
    app.run(debug=True)