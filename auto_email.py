import pyautogui as py
from time import sleep as sleep

py.PAUSE = 0.25
py.FAILSAFE = True

suportEmail = 'smb_web@support.whatsapp.com'
numbers = ["+5514998485030","+5514997843373","+5514997287014","+5514999065878","+5514998749211","+5514998393502","+5514996704436","+5514996355828","+5514998031157","+5514996481790","+5514997419359","+5514997656125","+5514996286799","+5514998595307","+5514996134962","+5514996492002","+5514999018400","+5514997321172","+5514991156483","+5514991055184","+5514998819143","+5514991328315"]

def text(i:int):
    py.write(f'Bom dia, prezados, meu chip número: { numbers[i] } foi banido, por favor, preciso do mesmo para trabalhar, sempre troco mensagens com meus clientes por meio dele, por favor, solicito o desbanimento o quanto antes, desde já agradeço!')

def openGmail():
    py.press('win')
    py.write('google')
    py.press('enter')
    py.write('gmail.com')
    py.press('enter')
    py.sleep(3)

def compose(i:int):
    py.press('c')
    py.write('smb')
    py.press('enter')
    py.press('tab')
    py.write(f'Numero banido { i } { numbers[i] }:')
    py.press('tab')
    text(i)
    py.hotkey('ctrl', 'enter')
    sleep(1)

def start():
    openGmail()
    for i in range(len(numbers)):
        compose(i)
    
    py.alert(text='OPERAÇÃO CONCLUIDA', title='ALERTA!', button='OK')

start()
