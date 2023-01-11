import mysql.connector
from flask import current_app, g

def get_db():
    if 'db' not in g:
        # g.db = mysql.connector.connect(
        #     host = current_app.config['DATABASE_HOST'],
        #     user = current_app.config['DATABASE_USER'], 
        #     password = current_app.config['DATABASE_PASSWORD'], 
        #     database = current_app.config['DATABASE']
        # )

        g.db = mysql.connector.connect(
            host = '192.168.100.55',
            user = 'remote', 
            password = 'remote124', 
            database = 'bambina')
        
        g.c = g.db.cursor(dictionary=True)

    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)


#Original

# import mysql.connector


# def get_db():
#     g = mysql.connector.connect(
#         host = '192.168.100.55',
#         user = 'remote', 
#         password = 'remote124', 
#         database = 'bambina')
        
#     c = g.cursor(dictionary=True)

#     return g, c

