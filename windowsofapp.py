import PySimpleGUI as sg

class windows_of_app:
    
    def tela_inicial(self):
        menu_def =[
            ['&Arquivo', ['&Novo_BD', '&Abrir_BD', '&Sair']],            
            ['&Ajuda', ['&Manual do Software', '&Sobre o Autor', ['&Linkedin', '&GitHub']]]
            ]

        layout = [
            [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],  
            [sg.Stretch(), sg.Button('Novo_BD', font=('Roboto', 36)), sg.Stretch()],
            [sg.Stretch(), sg.Button('Abrir_BD', font=('Roboto', 36)), sg.Stretch()]
            ]        
        return sg.Window('PyPass - Gerenciador de Senhas', element_justification='c', layout=layout, finalize=True, resizable=True)
     
    def inserir_dados(self):         
        layout = [
            [sg.Stretch(), sg.Text('Nome do serviço:', size=(20, 1)), sg.Input(key='-servico-'), sg.Stretch()],
            [sg.Stretch(), sg.Text('Nome do usuário:', size=(20, 1)), sg.Input(key='-user-'), sg.Stretch()],
            [sg.Stretch(), sg.Text('Senha:', size=(20, 1)), sg.Input(key='-senha-', password_char='*'), sg.Stretch()],
            [sg.Stretch(), sg.Text('Confirmar Senha:', size=(20, 1)), sg.Input(key='-confirmar-', password_char='*'), sg.Stretch()],
            [sg.Stretch(), sg.Button('Salvar_BD'), sg.Stretch(), ]            
            ]
        return sg.Window('PyPass - Guardar Senha', layout=layout, finalize=True, resizable=True)
    
    def guardar_senha(self):
        layout = [
            [sg.Text('Crie uma senha que você vai se lembrar depois. Use esta mesma senha para criar outros BDs!')],
            [sg.Stretch(), sg.Text('Senha_Mestra', size=(15, 1)), sg.Input(key='-mestra-', password_char='*'), sg.Stretch()],
            [sg.Stretch(), sg.Text('Senha_Mestra', size=(15, 1)), sg.Input(key='-novamente-', password_char='*'), sg.Stretch()],
            [sg.Stretch(), sg.Button('Salvar'), sg.Stretch()]
            
            ]
        return sg.Window('PyPass - Guardar Senha', layout=layout, finalize=True, resizable=True)
        
    def recuperar_senha(self):
        layout = [
            [sg.Text('Lembra da senha mestra?', font=('Any', 15))],
            [sg.Stretch(), sg.Text('Senha Mestra:', font=('Any', 12)), sg.Input(key='-password-', password_char='*', font=('Any', 12)), sg.Stretch()],
            [sg.Stretch(), sg.Button('Ok'), sg.Stretch()]
            ]
        return sg.Window('PyPass - Abrir Senha', layout=layout, finalize=True, resizable=True)
    
    def exibir(self, servicod, usuariod, senhad):
        self.servicod = servicod
        self.usuariod = usuariod
        self.senhad = senhad
        layout = [
            [sg.Stretch(), sg.Text('SENHAS RECUPERADAS COM SUCESSO', font=('Any', 15)), sg.Stretch()],
            [sg.Text('SERVIÇO', font=('Any', 12), size=(10, 1)), sg.Text(servicod, font=('Any', 12), size=(25, 1)), sg.Stretch()],
            [sg.Text('USUARIO', font=('Any', 12), size=(10, 1)), sg.Text(usuariod, font=('Any', 12), size=(25, 1)), sg.Button('Copiar_Usuario'), sg.Stretch()],
            [sg.Text('SENHA', font=('Any', 12), size=(10, 1)), sg.Text(senhad, font=('Any', 12), size=(25 , 1), key='-ver_senha-'), sg.Button('Copiar_Senha'), sg.Button('Ver_Senha'), sg.Stretch()],
            ]
        return sg.Window('PyPass - Visualizar Senhas', layout=layout, finalize=True, resizable=True)