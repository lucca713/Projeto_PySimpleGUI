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



janela = sg.Window('Login', layout)


while True:

    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        print('ok')
        
       
        
       #------------------janela login ---------------------         

    if event == 'New_login':
        event = janela.close() #fecha a janela anterior quando entrar para criar nova conta

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
            



#cinfig do banco de dados

link_bd  = 'https://cadastro-user-dc0d0-default-rtdb.firebaseio.com/'

requisicao = requests.post(f'{link_bd}/Nome.json', data= json.dumps(user))
requisicao = requests.post(f'{link_bd}/Senha.json', data= json.dumps(senha))
requisicao = requests.post(f'{link_bd}/Login.json', data= json.dumps(login))
                    
                           

if requisicao.status_code == 200:
    print('Dados enviados com sucesso para o Firebase.')
else:
    print('Falha ao enviar os dados para o Firebase.')

    """
    Criei a tela de criar usuario,

    fiz o codigo para mandar o novo usuario para o banco de dados

    falta fazer a parte do login funcionar com a senha e usuario certo de acordo com oq esta no banco de dados,

    fazer um campo de esqueci a senha.

    """