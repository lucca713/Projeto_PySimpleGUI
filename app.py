def fazer_login(usuario, senha):
    link_bd = 'https://cadastro-user-dc0d0-default-rtdb.firebaseio.com/'
    url = f"{link_bd}/Login.json"

    requisicao = requests.get(url)
    dados = requisicao.json()

    for chave, valor in dados.items():
        if valor["cliente"] == usuario and valor["password"] == senha:
            return True

    return False


import PySimpleGUI as sg
import requests
import json

layout = [  
[sg.Text('Usuário')],
[sg.Input(key='usuario')],
[sg.Text('Senha')],
[sg.Input(key='senha')],
[sg.Button('login'), sg.Button('Criar uma conta', key='New_login')],
[sg.Text('', key='mensagem')],
]

#evento tipo o baotao que vc clica (a ação) o valor é aquilo que ele retora ou faz

janela = sg.Window('Login', layout)


while True:

    event, values = janela.read() #eventos e valores da janela principal (layout)
    
    if event == 'login': #para verificar se o login existe no Banco de dados
        print('ok')
        usuario = values['usuario']
        senha = values['senha']

        if fazer_login(usuario, senha):
            sg.popup('Login bem-sucedido')
        else:
            sg.popup('Usuário ou senha inválidos')
       
        



       #------------------janela criar a conta ---------------------         

    elif event == 'New_login':
        janela.hide() #Esconde a janela anterior quando entrar para criar nova conta

        Criar_conta = [

            #aqui fica os novos valores 
              
            [sg.Text('Nome de usuario')],
            [sg.Input(key='novo_usuario')],
            [sg.Text('Senha')],
            [sg.Input(key='nova_senha')],
            [sg.Button('Criar'), sg.Button('Cancelar') ],
            
        ]
        nova_janela = sg.Window('Não tenho uma conta', Criar_conta)
        while True:

            #novos eventos e valores da nova janela de criar conta 
            new_event, new_values = nova_janela.read() 
            if new_event == 'Fechar' or new_event == sg.WINDOW_CLOSED:
                break #se o evento for de fechar a janela ela vai fechar 
            elif new_event == 'Criar' :

                user = {'cliente': new_values['novo_usuario']}

                senha = {'password': new_values['nova_senha']}

                login = {'cliente': new_values['novo_usuario'],
                         
                         'password': new_values['nova_senha']
                         } 
                nova_janela.close() #fecha a janela nova janela que é a do cadastro usuario
                janela.un_hide() #abre a janela de login
            
#------- funcionalidade do botão cancelar -----------

            elif new_event == 'Cancelar' or new_event == sg.WINDOW_CLOSED:
                nova_janela.close() #fecha a janela nova janela que é a do cadastro usuario
                janela.un_hide() #abre a janela de login
        
        
                    
    if event == sg.WINDOW_CLOSED:#ele fecha a janela principal
        break           









#cinfig do banco de dados

link_bd  = 'https://cadastro-user-dc0d0-default-rtdb.firebaseio.com/'

requisicao = requests.post(f'{link_bd}/Nome.json', data= json.dumps(user))
requisicao = requests.post(f'{link_bd}/Senha.json', data= json.dumps(senha))
requisicao = requests.post(f'{link_bd}/Login.json', data= json.dumps(login))
requisicao = requests.get(f'{link_bd}.json')

                           

if requisicao.status_code == 200:
    print('Dados enviados com sucesso para o Firebase.')
else:
    print('Falha ao enviar os dados para o Firebase.')

    """
    falta: quando o usuario fazer o login levar ele para uma tela feita em django por mim.
    
    fazer um botaão esqueci a senha 

    fazer ele virar um executavel

    corrigir bugs
    """