from pytubefix import YouTube,Playlist
import os
from time import sleep

def video(): #Download de um vídeo no youtube
    print('-='*46)
    URL=str(input('Digite a URL do vídeo que você deseja baixar: '))
    yt=YouTube(f'{URL}')
    print('-='*46)
    print(f'Baixando o vídeo: \033[34m{yt.title}\033[m\nDo autor: \033[34m{yt.author}\033[m')
    print('-='*46)
    audio=yt.streams.filter(progressive=True).first()
    if not os.path.exists(r'C:\Users\pedro\Desktop\Vídeo'):
        print('\033[32mCriando a pasta Vídeo na área de trabalho e salvando o arquivo',end='')
        for c in range(0,3):
            print('.',end='')
            sleep(0.5)
        print('\033[m')
        os.mkdir(r'C:\Users\pedro\Desktop\Vídeo')
    else:
        print('\033[32mSalvando o arquivo na pasta Vídeo na área de trabalho',end='')
        for c in range(0,3):
            print('.',end='')
            sleep(0.5)
        print('\033[m')
    print('-='*46)
    audio.download(output_path=r'C:\Users\pedro\Desktop\Vídeo')

def musica(): #Download somente do áudio de um vídeo no youtube
    print('-='*46)
    URL=str(input('Digite a URL da faixa que você deseja baixar: '))
    yt=YouTube(f'{URL}')
    print('-='*46)
    print(f'Baixando a faixa: \033[34m{yt.title}\033[m\nDo autor: \033[34m{yt.author}\033[m')
    print('-='*46)
    audio=yt.streams.filter(only_audio=True).first()
    if not os.path.exists(r'C:\Users\pedro\Desktop\Músicas'):
        print('\033[32mCriando a pasta Música na área de trabalho e salvando a faixa',end='')
        for c in range(0,3):
            print('.',end='')
            sleep(0.5)
        print('\033[m')
        os.mkdir(r'C:\Users\pedro\Desktop\Músicas')
    else:
        print('\033[32mSalvando a faixa na pasta Música na área de trabalho',end='')
        for c in range(0,3):
            print('.',end='')
            sleep(0.5)
        print('\033[m')
    print('-='*46)
    audio.download(output_path=r'C:\Users\pedro\Desktop\Músicas')

def playl():
    #Definir qual interesse na playlist
    print('=-'*18)
    URL=str(input('Digite a URL da playlist: '))
    P=Playlist(f'{URL}')

    print('--'*12,'MENU','--'*12)
    print('1 -> Baixar os vídeos completos da playlist')
    print('2 -> Baixar somente os aúdios dos vídeos da playlist')
    print('--'*27)
    while True:
        try:
            Esc=int(input('Digite a opção desejada: '))
            if Esc in range(1,3):
                break
            else:
                print('\033[31mERRO! Digite um número válido.\033[m')
        except:
                print('\033[31mERRO! Digite um número.\033[m')
    print('--'*27)
    
    if Esc==1: #Baixar os vídeos completos da playlist
        while True: #Definição do início
            try:
                Num=int(input('Digite quantos desses vídeos você deseja iniciar o download \033[32m(Não digite nada para iniciar da primeira)\033[m: '))
                if 1<=Num<=len(P):
                    print(f'\033[34mDefinido para baixar desde o vídeo {Num}.\033[m')
                    Ini=Num
                    break
                else:
                    print('\033[31mERRO! Digite um número válido.\033[m')
            except TypeError:
                    print('\033[31mERRO! Digite um número.\033[m')
            except: 
                    print(f'\033[34mDefinido para baixar desde o primeiro vídeo.\033[m')
                    Ini=0
                    break
            
        while True: #Definição do limite de download
            try:
                Num=int(input('Certo. Agora digite quantos desses vídeos você deseja realizar o download \033[32m(Não digite nada para baixar todos)\033[m: '))
                if 1<=Num<=len(P):
                    print(f'\033[34mDefinido para baixar até o vídeo {Num}.\033[m')
                    Lim=Num
                    break
                else:
                    print('\033[31mERRO! Digite um número válido.\033[m')
            except TypeError:
                    print('\033[31mERRO! Digite um número.\033[m')
            except:
                    print(f'\033[34mDefinido para baixar todos os {len(P)} vídeos da playlist.\033[m')
                    Lim=len(P)
                    break
                    print('-='*46)
        
        if not os.path.exists(r'C:\Users\pedro\Desktop\Vídeo'): #Verificar a existência do local para salvar os arquivos
            print('\033[32mCriando a pasta Vídeo na área de trabalho e salvando os arquivos',end='')
            for c in range(0,3):
                print('.',end='')
                sleep(0.5)
            print('\033[m')
            os.mkdir(r'C:\Users\pedro\Desktop\Vídeo')
        else:
            print('\033[32mSalvando os arquivos na pasta Vídeo na área de trabalho',end='')
            for c in range(0,3):
                print('.',end='')
                sleep(0.5)
            print('\033[m')
        print('-='*46)

        for Atual in P.videos[Ini:Lim]: #Download dos vídeos
                Atual.streams.filter(progressive=True).first().download(output_path=r'C:\Users\pedro\Desktop\Vídeo')
    
    if Esc==2: #Baixar somente os aúdios dos vídeos da playlist
        while True: #Definição do início
            try:
                Num=int(input('Digite por qual das músicas você deseja iniciar o download \033[32m(Não digite nada para iniciar da primeira)\033[m: '))
                if 1<=Num<=len(P):
                    print(f'\033[34mDefinido para baixar desde a faixa {Num}.\033[m')
                    Ini=Num
                    break
                else:
                    print('\033[31mERRO! Digite um número válido.\033[m')
            except TypeError:
                    print('\033[31mERRO! Digite um número.\033[m')
            except:
                    print(f'\033[34mDefinido para baixar desde a primeira faixa\033[m')
                    Ini=0
                    break
        print('-='*46)

        while True: #Definição do limite de download
            try:
                Num=int(input('Certo. Agora digite quantos dessas músicas você deseja realizar o download \033[32m(Não digite nada para baixar todos)\033[m: '))
                if 1<=Num<=len(P):
                    print(f'\033[34mDefinido para baixar até a faixa {Num}.\033[m')
                    Lim=Num
                    break
                else:
                    print('\033[31mERRO! Digite um número válido.\033[m')
            except TypeError:
                    print('\033[31mERRO! Digite um número.\033[m')
            except:
                    print(f'\033[34mDefinido para baixar todos as {len(P)} faixas da playlist.\033[m')
                    Lim=len(P)
                    break
        print('-='*46)

        if not os.path.exists(r'C:\Users\pedro\Desktop\Músicas'): #Verificar a existência do local para salvar os arquivos
            print('\033[32mCriando a pasta Música na área de trabalho e salvando as faixas',end='')
            for c in range(0,3):
                print('.',end='')
                sleep(0.5)
            print('\033[m')
            os.mkdir(r'C:\Users\pedro\Desktop\Músicas')
        else:
            print('\033[32mSalvando as faixas na pasta Música na área de trabalho',end='')
            for c in range(0,3):
                print('.',end='')
                sleep(0.5)
            print('\033[m')
        print('-='*46)

        for Atual in P.videos[Ini:Lim]: #Download das músicas
                Atual.streams.filter(only_audio=True).first().download(output_path=r'C:\Users\pedro\Desktop\Músicas')
