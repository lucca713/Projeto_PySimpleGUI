import requests
import json
import PySimpleGUI as sg
def fazer_login(usuario, senha):
    
    link_bd = 'https://caduser-40a03-default-rtdb.firebaseio.com/' # link do bd
    url = f"{link_bd}/Login.json" #transforma as informações do banco em um dicionario json

    requisicao = requests.get(url) #ele da um get (pega) as informações do banco de dados 
    dados = requisicao.json() # tranforma as informações em uma arquivo json

    for chave, valor in dados.items(): # ele começa um loop lendo chaves e valores do banco de dados
        if valor["cliente"] == usuario and valor["password"] == senha:
            #aqui se o valor da chave cliente for igual oque o usuario digitou e a mesma coisa para senha ele retorna true
            return True

    return False

def Banco_dado():
    

    link_bd  = 'https://caduser-40a03-default-rtdb.firebaseio.com/'
    global requisicao
    requisicao = requests.post(f'{link_bd}/Nome.json', data= json.dumps(user))
    requisicao = requests.post(f'{link_bd}/Senha.json', data= json.dumps(senha))
    requisicao = requests.post(f'{link_bd}/Login.json', data= json.dumps(login))


def recuperar_senha(usuario1):
    link_bd = 'https://caduser-40a03-default-rtdb.firebaseio.com/' # link do bd
    url = f"{link_bd}/Login.json" #transforma as informações do banco em um dicionario json

    requisicao = requests.get(url) #ele da um get (pega) as informações do banco de dados 
    dados = requisicao.json() # tranforma as informações em uma arquivo json

    for chave, valor in dados.items(): # ele começa um loop lendo chaves e valores do banco de dados
        if valor.get("cliente")== usuario1: #usa só nome para pegar a senha
           senha1 = valor.get('password')
           if senha1: 
            sg.popup(senha1)