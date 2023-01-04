import mysql.connector

def get_db():
    g = mysql.connector.connect(
        host = '192.168.100.55',
        user = 'remote', 
        password = 'remote124', 
        database = 'bambina')
        
    c = g.cursor(dictionary=True)

    return g, c
