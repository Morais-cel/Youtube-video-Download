from Func_dev import musica,video,playl
from time import sleep
def HUD():
    print('=-'*22)
    print(f'{'YOUTUBE DOWNLOADER':>30}')
    print('=-'*22)
    print('1 -> BAIXAR VÍDEO NO YOUTUBE.')
    print('2 -> BAIXAR MÚSICA NO YOUTUBE.')
    print('3 -> BAIXAR PLAYLIST NO YOUTUBE.')
    print('4 -> SAIR.')
    print('=-'*18)
    while True:
        try:
            Esc=int(input('Digite a opção desejada: '))
            if 1<=Esc<=4:
                break
            else:
                print('\033[31mERRO! Digite um valor válido!\033[m')
        except:
            print('\033[31mERRO! Digite um valor númerico!\033[m')
    if Esc==1: #Download vídeo
        video()
    elif Esc==2: #Download música
        musica()
    elif Esc==3: #Sownload playlist
        playl()
    else: #Sair
        print('-='*9)
        print('Saindo',end='')
        for c in range(0,3):
            print('.',end='')
            sleep(0.5)
        print('')
        print('-='*9)