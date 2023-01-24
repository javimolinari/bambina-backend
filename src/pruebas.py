
#Pruebas sobre el usuario y contraseña


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
           
            token, date = code_generator()

            if r['gmantener'] == 'si':
                tp = add_days(date, 14)
            else:
                tp = add_days(date, 1)

            SIS_Usuarios.gid_usuario = usu['gid_usuario']
            SIS_Usuarios.gtoken = token
            SIS_Usuarios.gfechaexpiracion = tp
            SIS_Usuarios.update_token_by_id()

            #Asigno el token nuevo generado para cargar en session
            numtoken = token

        else:
            #Asigno el token activo desde de BBDD para cargar en session
            numtoken = usu['Token']

        #Creo la nueva session del token y asocio las pantallas permitidas
        newlog = {numtoken: []}

        for p in pantallas:
            newlog[numtoken].append([p['Pantalla'], p['Ruta']])

        #Cargo este nuevo log en el diccionarios de logs
        logs[numtoken] = [newlog[numtoken]]

        return jsonify(newlog)
        



        #Funciones anteriores
        logs[numtoken] = {"gtoken":numtoken, 'gpantallas': []}

        for p in pantallas:
            logs[numtoken]['gpantallas'].append(p['Pantalla'] + '|' + p['Ruta'])

        return jsonify(logs[numtoken])

    except Exception as e:
        return jsonify("Entre en error en get_usuario", e)

@app.route('/api/not_expired', methods=['POST'])
def get_usuario_token_by_token():
    try:
        #Comprueba que el token se encuentre en el diccionario de logs. Si es así, retorna los datos
        #del usuario con el token solamente. Sino, crea la sesion

        # if request.json in logs:
        #     return jsonify(logs[request.json])

        #Get de los datos del usuario por token
        from clases.Usuarios.SIS_Usuarios import SIS_Usuarios
        SIS_Usuarios = SIS_Usuarios()
        SIS_Usuarios.gtoken = request.json
        datos = SIS_Usuarios.get_usuario_by_token()

        #Si no existe, devuelve close
        if not datos:
            return jsonify ("not logged")

        if datos['Expiracion'] < 0:
            SIS_Usuarios.gid_usuario = datos['gid_usuario']
            SIS_Usuarios.delete_token_usuario()

            return jsonify ("expired")

        #Creo la session del usuario en memoria para luego cargar los permisos
        logs[datos['Token']] = {}
        logs[datos['Token']]['Pantallas'] = []
        logs[datos['Token']]['Expired'] = datos['Fecha expiración']

        from clases.Usuarios_Pantallas.SIS_Usuarios_Pantallas import SIS_Usuarios_Pantallas
        SIS_Usuarios_Pantallas = SIS_Usuarios_Pantallas()
        SIS_Usuarios_Pantallas.gid_usuario = datos['gid_usuario']
        pantallas = SIS_Usuarios_Pantallas.get_usuarios_pantallas()

        for p in pantallas:
            logs[datos['Token']].append([p['Pantalla'],p['Ruta']])

        return jsonify(logs[datos['Token']])

    except Exception as e:
        return jsonify("Entre en error en get_usuario_token_by_token", e)



        from clases.Usuarios.SIS_Usuarios_Token import SIS_Usuarios_Token
        from datetime import datetime

        #Busca los datos relacionados el token recibido
        SIS_Usuarios_Token = SIS_Usuarios_Token()
        SIS_Usuarios_Token.gtoken = request.json

        datos = SIS_Usuarios_Token.get_usuario_token_by_token()

        #Si no existe, devuelve close
        if not datos:
            return jsonify ("close")

        #Si existe, comprueba que no esté expirado. Si lo está, borra el token de la sesion también
        if datos['gfechaexpiracion'] < datetime.now():
            SIS_Usuarios_Token.gid_token = datos['gid_token']
            SIS_Usuarios_Token.del_usuario_token()

            session.pop(datos['gtoken'])

            return jsonify ("close")

        return jsonify ("ok")

    # except Exception as e:
        return jsonify("Entre en error en get_usuario_token_by_token", e)