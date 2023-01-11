from datetime import datetime
from datetime import timedelta
from random import sample

numeros= ['0','1','2','3','4','5','6','7','8','9']
caracter = ['!','#','$','%','&','*','-','_','¡','?','¿','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def code_generator():
    token = ''
    date = datetime.now()
    time =  datetime.timestamp(date)

    for i in sample(caracter, 28):
        token += i

    for i in sample(numeros, 10):
        token += i

    for i in str(time):
        if i == '.':
            continue

        token += i

    for i in sample(numeros, 10):
        token += i

    for i in sample(caracter, 28):
        token += i

    return token, date


def add_days(time, days):
    return time + timedelta(days = days)
