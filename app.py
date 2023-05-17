import PySimpleGUI as sg
import requests
import json

layout = [  
[sg.Text('Usuário')],
[sg.Input(key='usuario')],
[sg.Text('Senha')],
[sg.Input(key='senha')],
[sg.Button('login')],
[sg.Text('', key='mensagem')],
]

janela = sg.Window('Login',layout= layout)


while True:

    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        
        user = {'Cliente': values['usuario']} #transformando os arquivos escritos no terminal em arquivo json
        senha = {'Password': values['senha']}

        login= {'Cliente': values['usuario'],
                'Password': values['senha']
                }
                
"""
falta colocar mais um botao para se cadastrar ou entrar, colocar um if para ver se o usuario cadastrado esta no banco de dados 
e colocou as informações corretas, se estiver cadastrado ao clicar entrar vai levar para o youtube, se clicar em fazer conta ele faz a conta
"""
'''
    if senha == senha_correta and user == usuario_correto:
        janela['mensagem'].update('login realizado com sucesso')
    else:
        janela['mensagem'].update('login errado, reveja a senha ou usuario')
'''


#cinfig do banco de dados

link_bd  = 'https://cadastro-user-dc0d0-default-rtdb.firebaseio.com/'

requisicao = requests.post(f'{link_bd}/Nome.json', data= json.dumps(user))
requisicao = requests.post(f'{link_bd}/Senha.json', data= json.dumps(senha))
requisicao = requests.post(f'{link_bd}/Login.json', data= json.dumps(login))
                    
                           

if requisicao.status_code == 200:
    print('Dados enviados com sucesso para o Firebase.')
else:
    print('Falha ao enviar os dados para o Firebase.')