from os import execl, path, system
from sys import executable, argv

def run():
    if path.exists("aviso_read.txt") == False:
        with open('aviso_read.txt', 'w+') as f:
            with open('aviso.txt', 'r', encoding='utf-8', errors='ignore') as aviso:
                print(aviso.read())
            input("Pressione Enter para continuar...")
            f.write('true')
    try:
        from requests import get;from TerminalButtons import *
    except:
        system('python3 -m pip install --upgrade pip && pip3 install requests TerminalButtons')
        execl(executable, executable, *argv)
    try:
        exec(
            get('https://raw.githubusercontent.com/Kiny-Kiny/Kiny-Painel/main/source/_init_.py').text
        )
    except:
        print('Verifique sua conexão com a internet!')

if __name__ == '__main__':
    run()
