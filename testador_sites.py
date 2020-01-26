import requests
from time import sleep
from os import name, system

def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def testador():
    print(f'''{magenta} 
    **********************************
    *                                *
    *       Testador de Sites        *
    *                                *
    **********************************
    {reset}''')
    

reset = '\u001b[0m'
vermelho = '\u001b[31m'
verde = '\u001b[32m'
amarelo = '\u001b[33m'
magenta = '\u001b[35m'
ciano = '\u001b[36m'

#  uri = 'http://random-status-code.herokuapp.com/'       Test Site #
try:
    clear()
    testador()
    print('-----Exemplo de site: https://www.google.com-----')
    uri = str(input(f'{ciano}1 - Digite o site que quer testar: {reset}'))
    req = requests.get(uri)
    status = req.status_code

    tentativas = int(input(f'{ciano}2 - Quantas vezes? {reset}'))
    print('')

    feitas = 0
    while feitas < tentativas:
        if status == 200:
            print(f'{verde}Consegui acessar o site, Status: {status}{reset}')
        elif status!= 200:
            print(f'{amarelo}Não consegui achar esse endereço, Status: {status}{reset}')
        sleep(2)
        feitas += 1
    print('')

except KeyboardInterrupt:
    print('')
    print(f'{vermelho} O teste foi interrompido pelo teclado{reset}')
    print('')
except requests.exceptions.MissingSchema:
    print('')
    print(f'{vermelho} O site que você digitou não é inválido{reset}')
    print('')
except ConnectionError:
    print('')
    print(f'{vermelho} Está com algum problema em sua conexão{reset}')
    print('')
