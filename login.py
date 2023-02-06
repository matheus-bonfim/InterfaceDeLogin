import PySimpleGUI as sg

class Register():
    def __init__(self, name, key, bank):
        self.name =  name 
        self.key = key
        self.perfil = [name, key]
        self.bank = bank
    def getprofile(self):
        return self.perfil
    def reg(self):
        self.bank.append(self.perfil)

banco = []

def inicial():
    layout = [
        [sg.Text('Já tem conta?')],
        [sg.Button('Sim'), sg.Button('Não')]
    ]
    return sg.Window('Sistema de login', layout=layout, finalize=True)


def pagLogin():
    layout = [

            [sg.Text('Usuário')],
            [sg.Input(key='usuario')],
            [sg.Text('Senha')],
            [sg.Input(key='senha')],
            [sg.Button('Login'), sg.Button('Voltar')],
            [sg.Text('', key='mensagem')]
            ]
    
    return sg.Window('Login', layout=layout, finalize=True)

def pagReg():
    layout = [
        [sg.Text('Crie seu usuário e sua senha')],
        [sg.Text('Usuário')],
        [sg.Input(key='usuarioR')],
        [sg.Text('Senha')],
        [sg.Input(key='senhaR')],
        [sg.Button('Registrar'), sg.Button('Voltar')],
        [sg.Text('',key='mensagem')]  
    ]
    return sg.Window('Registrar',layout=layout, finalize=True)

janelaInicial, janelaRegistrar, janelaLogar = inicial(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break

    if window == janelaInicial and event == 'Não':
        janelaInicial.hide()
        janelaRegistrar = pagReg()

    if window == janelaInicial and event == 'Sim':
        janelaInicial.hide()
        janelaLogar = pagLogin()

    
        
 

    if window == janelaRegistrar:

        if event == 'Voltar':
            janelaRegistrar.hide()
            janelaInicial.un_hide()
    
        if event == 'Registrar':
            
            print('oi')
            usuario = values['usuarioR']
            senha = values['senhaR']

            if len(usuario) >= 5 and len(senha) >= 5:

                perfil = Register(usuario, senha, banco)
                perfil.reg()
                print(banco)
                janelaRegistrar['mensagem'].update("Registrado!")
            
            else:

                janelaRegistrar['mensagem'].update("Usuário e senha devem ter mais de 5 caracteres!")
    
    if window == janelaLogar:

        if event == 'Voltar':
            janelaLogar.hide()
            janelaInicial.un_hide()
        
        elif event == 'Login':

            usuario = values['usuario']
            senha = values['senha']
            perfil = [usuario, senha]

            if perfil in banco:
                print("acesso aprovado")
                janelaLogar['mensagem'].update('Acesso Aprovado')

            else: 
                print("acesso negado")
                janelaLogar['mensagem'].update('Acesso Negado')










