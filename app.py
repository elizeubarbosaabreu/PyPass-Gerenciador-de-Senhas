import pyAesCrypt, os, clipboard, time, webbrowser
import PySimpleGUI as sg
from windowsofapp import windows_of_app
# 
#      ____        ____                       
#     |  _ \ _   _|  _ \ __ _ ___ ___         
#     | |_) | | | | |_) / _` / __/ __|  _____ 
#     |  __/| |_| |  __/ (_| \__ \__ \ |_____|
#     |_|    \__, |_|   \__,_|___/___/        
#            |___/                            
#       ____                          _           _                  _      
#      / ___| ___ _ __ ___ _ __   ___(_) __ _  __| | ___  _ __    __| | ___ 
#     | |  _ / _ \ '__/ _ \ '_ \ / __| |/ _` |/ _` |/ _ \| '__|  / _` |/ _ \
#     | |_| |  __/ | |  __/ | | | (__| | (_| | (_| | (_) | |    | (_| |  __/
#      \____|\___|_|  \___|_| |_|\___|_|\__,_|\__,_|\___/|_|     \__,_|\___|
#                                                                           
#      ____             _               
#     / ___|  ___ _ __ | |__   __ _ ___ 
#     \___ \ / _ \ '_ \| '_ \ / _` / __|
#      ___) |  __/ | | | | | | (_| \__ \
#     |____/ \___|_| |_|_| |_|\__,_|___/
#                                       

# iniciadores
janela = windows_of_app()    

sg.theme('Reddit')

janela1, janela2, janela3, janela4 = janela.tela_inicial(), None, None, None

while True:
    window, event, values = sg.read_all_windows()     
####   
    if window == janela1 and event == sg.WIN_CLOSED or event == 'Sair':
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == sg.WINDOW_CLOSED or event == 'Salvar':
        janela3.hide()
        janela1.un_hide()
    if window == janela4 and event == sg.WINDOW_CLOSED:
        janela4.hide()
        janela1.un_hide()

    if window == janela1 and event == 'Novo_BD':        
        janela2 = janela.inserir_dados()
        janela1.hide()
    if window == janela2 and event == 'Salvar_BD':
        if values['-senha-'] == values['-confirmar-'] and values['-senha-'] != '':
            senha = values['-senha-']
            servico = values['-servico-']
            usuario = values['-user-']
            janela3 = janela.guardar_senha()
            janela2.hide()
        else:
            sg.popup_ok_cancel('Erro de senha!', 'As senhas não conferem ou campo estão vazios')
    if window == janela3 and event == 'Salvar':
        if values['-mestra-'] == values['-novamente-'] and values['-mestra-'] != '':
            password_confirma  = values['-novamente-']            
            filename = sg.popup_get_file(
                'Escolha onde quer guardar a senha',
                save_as = True,
                file_types = (('TXT', '*.txt'),)
                )             
            filename_cripta = filename + ".aes"
            bufferSize = 64 * 1024
            with open(filename, 'w') as f:
                f.write(
f'''{servico}
{usuario}
{senha}
'''
                        )
            pyAesCrypt.encryptFile(filename, filename_cripta, password_confirma, bufferSize)
            os.remove(filename)
            
        else:
            sg.popup_ok_cancel(
                'Erro de senha!',
                'As senhas não conferem ou campo estão vazios',
                text_color = 'red'
                )
        
    try:   
        if window == janela1 and event == 'Abrir_BD':
            arquivo_cripto = sg.popup_get_file('Onde está a senha que você quer recuperar?')
            janela2 = janela.recuperar_senha()
            janela1.hide()
        
        if window == janela2 and event == 'Ok':
                  
            senha = values['-password-']
            bufferSize = 64 * 1024
               
            pyAesCrypt.decryptFile(arquivo_cripto, "temp.txt", senha, bufferSize)
            
            with open("temp.txt", "r") as txt:
                resultado = txt.readlines()
            txt.close()        
            janela2.hide()
            os.remove('temp.txt')
            servicod = resultado[0]
            usuariod = resultado[1]
            senhad = '*******'       
            janela4 = janela.exibir(servicod, usuariod, senhad)
            
        if window == janela4 and event == 'Copiar_Usuario':
            clipboard.copy(resultado[1])
            sg.popup_timed('"Nome de Usuário" na área de transferência', 'Use CTRL+C para colar')
        if window == janela4 and event == 'Copiar_Senha':
            clipboard.copy(resultado[2])
            sg.popup_timed('"Senha" na área de transverência', 'Use CTRL+C para colar')
        if window == janela4 and event == 'Ver_Senha':
            senhad = resultado[2]            
            sg.popup_timed('Senha Recuperada',
                           f'Olá sua senha é: {senhad}',
                           font=('Any', 10),
                           text_color = 'green'
                           )
    except:
        sg.Popup('ERRO!',
                 'Senha ou arquivo errado',
                 text_color = 'red')
        janela2.hide()
    if window == janela1 and event == 'Manual do Software':
        sg.Popup('MANUAL DO USUARIO',
                 'PyPass - Gerenciador de Senhas é um software criado inteiramente em Python tendo por função armazenar suas senhas de maneira segura e criptografada...',
                 'As senhas serão visualizadas somente com a digitação da SENHA MESTRA que deve ser rmazenada em local seguro e não deve ser esquecida...',
                 'Não nos responsabilizamos pelo esquecimento ou mal uso de suas senhas...'
                )
    if window == janela1 and event == 'Linkedin':
        webbrowser.open('https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/')
    if window == janela1 and event == 'GitHub':
        webbrowser.open('https://github.com/elizeubarbosaabreu/Lorem-Ipsum-Generator.git')
        
janela1.close()
