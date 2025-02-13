from flet import *
import os
import requests
from pytubefix import YouTube

aux=1
url_glb='https://youtu.be/L8OesNa-pkA?si=sp6eN2gNl9Na998Q'
thmb_glb='default'
autor_glb='default'
titulo_glb='default'
dur_glb_m='default'

def gui(janela: Page): 
    def Menu(e): #Restarte
        janela.clean()
        inicio()

    def yout_inf(): #Buscar informações do conteúdo no youtube
        global thmb_glb,autor_glb,titulo_glb,dur_glb_m

        yt=YouTube(url_glb)

        thmb_glb=yt.thumbnail_url
        titulo_glb=yt.title
        autor_glb=yt.author
        dur_glb_s=yt.length
        dur_glb_m=str(round(dur_glb_s/60,2)).replace('.',':') 

    def Baix_Thumb(e): #Baixar thumbnails

        thmb_dl= requests.get(thmb_glb)

        if not os.path.exists("C:/Users/pedro/Desktop/Youtube_Video_DownloadThumbnail"):
            os.makedirs("C:/Users/pedro/Desktop/Youtube_Video_Download/Thumbnail")
        with open(f"C:/Users/pedro/Desktop/Youtube_Video_Download/Thumbnail/{autor_glb} Thumb.png", "wb") as fp:
            fp.write(thmb_dl.content)

    def Baix_Video(e): #Baixar vídeos
        yt=YouTube(url_glb)
        video=yt.streams.filter(progressive=True).first()
        if not os.path.exists("C:/Users/pedro/Desktop/Youtube_Video_Download/Videos"):
            os.makedirs("C:/Users/pedro/Desktop/Youtube_Video_Download/Videos")
        video.download(output_path="C:/Users/pedro/Desktop/Youtube_Video_Download/Videos")

    def Baix_Music(e): #Baixar músicas
        yt=YouTube(url_glb)
        audio=yt.streams.filter(only_audio=True).first()
        if not os.path.exists("C:/Users/pedro/Desktop/Youtube_Video_Download/Audios"):
            os.makedirs("C:/Users/pedro/Desktop/Youtube_Video_Download/Audios")
        audio.download(output_path="C:/Users/pedro/Desktop/Youtube_Video_Download/Audios")

    def Esc_Baixar(e): #Escola entre baixar música ou vídeo
            global aux
            if aux==1: 
                Baix_Video(e)
            elif aux==2:
                Baix_Music(e)

    def process_baix(e): #Terceira tela (Download de músicas e vídeos)
        janela.window.width = 900
        janela.window.height = 300
        janela.window.resizable = False
        janela.clean()

        yout_inf()


        Img=Image(
            src=f'{thmb_glb}',
            width=350,
            height=200,
            fit=ImageFit.FILL,
            border_radius=border_radius.all(5),
        )

        Cancelar=Button( #Botão cancelar
                text='Cancelar',
                icon=Icons.CANCEL_OUTLINED,
                icon_color=Colors.WHITE,
                color=Colors.WHITE,
                on_click=Menu)
        
        Voltar=Button( #Botão voltar
                text='Voltar',
                icon=Icons.ARROW_BACK,
                icon_color=Colors.WHITE,
                color=Colors.WHITE,
                on_click=process_url)
        
        Download=Button( #Botão download
                text='Baixar',
                icon=Icons.FILE_DOWNLOAD_SHARP,
                icon_color=Colors.WHITE,
                color=Colors.WHITE,
                on_click=Esc_Baixar)

        Thumb=Button( #Botão thumb
                text='Baixar thumb',
                icon=Icons.IMAGE,
                icon_color=Colors.WHITE,
                color=Colors.WHITE,
                on_click=Baix_Thumb)
        
        inf_tit=Container( #Informações do título do vídeo
            content=Text(f'{titulo_glb}'),
            alignment=alignment.center_left,
            width=435,
            height=32,
            bgcolor=Colors.WHITE10,
            border_radius=border_radius.all(5),
            padding=5
            )
        
        inf_aut=Container( #Informações do autor do vídeo
            content=Text(f'{autor_glb}'),
            alignment=alignment.center_left,
            width=435,
            height=32,
            bgcolor=Colors.WHITE10,
            border_radius=border_radius.all(5),
            padding=5
            )

        inf_dur=Container( #Informações da duração do vídeo
            content=Text(f'{dur_glb_m} min',
                        size=15),
            alignment=alignment.center_left,
            width=80,
            height=32,
            bgcolor=Colors.WHITE10,
            border_radius=border_radius.all(5),
            padding=5
            )

        titulo=Row( #Texto 'Titulo'
            spacing=-5,
            controls=[
        Container(
            content=Text('Título',
                    color=Colors.WHITE,
                    size=15),
            alignment=alignment.center_left,
            width=50,
            height=32,
            border_radius=border_radius.all(5),
            padding=5
        ),
        Container(
            content=Icon(
                    name=Icons.ARROW_FORWARD_SHARP,
                    color=Colors.WHITE,
                    size=15),
            width=30,
            height=32,
            border_radius=border_radius.all(5),
            padding=5,
            alignment=alignment.center_left,
        )])

        autor=Row( #Texto 'Autor'
            spacing=-5,
            controls=[
        Container(
            content=Text('Autor',
                    color=Colors.WHITE,
                    size=15),
            alignment=alignment.center_left,
            width=50,
            height=32,
            border_radius=border_radius.all(5),
            padding=5
        ),
        Container(
            content=Icon(
                    name=Icons.ARROW_FORWARD_SHARP,
                    color=Colors.WHITE,
                    size=15),
            width=30,
            height=32,
            border_radius=border_radius.all(5),
            padding=5,
            alignment=alignment.center_left,
        )])

        duracao=Row( #Texto 'Duração'
            spacing=-5,
            controls=[
        Container(
            content=Text('Duração',
                    color=Colors.WHITE,
                    size=15),
            alignment=alignment.center_left,
            width=68,
            height=32,
            border_radius=border_radius.all(5),
            padding=5
        ),
        Container(
            content=Icon(
                    name=Icons.ARROW_FORWARD_SHARP,
                    color=Colors.WHITE,
                    size=15),
            width=30,
            height=32,
            border_radius=border_radius.all(5),
            padding=5,
            alignment=alignment.center_left,
        )])
        
        Coluna1=Column(alignment=MainAxisAlignment.START,
                height=400,
                controls=[
                Img,
                Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                    width=350,
                    controls=[
                    Cancelar,
                    Thumb
                ])
        ])

        Coluna2=Column(alignment=MainAxisAlignment.START,
                height=400,
                controls=[
                Row(spacing=-5,
                    controls=[
                    titulo,
                    inf_tit
                ]),
                Row(spacing=-5,
                    controls=[
                    autor,
                    inf_aut
                ]),
                Row(spacing=-5,
                    controls=[
                    duracao,
                    inf_dur
                ])   
        ])

        Coluna3=Column(alignment=MainAxisAlignment.END,
                height=240,
                width=505,
                controls=[
                Row(alignment=MainAxisAlignment.END,
                    controls=[
                    Voltar,
                    Download,
                ])])

        janela.add(
            Row(alignment=(MainAxisAlignment.START),
                controls=[
                Coluna1,
                Stack(controls=
                        [Coluna2,
                        Coluna3
            ])]))

    def process_url(e): #Segunda tela=
        janela.window.width = 700
        janela.window.height = 205
        janela.window.resizable = False
        janela.clean()
        janela.update()

        def desb(e): #Processo de bloquear e desbloquar o botao prosseguir
            if url.value=='':
                Prosseguir.disabled = True
                janela.update()
            else:
                Prosseguir.disabled = False
                janela.update()

        def func_def(e):
            global aux
            if aux==3:
                baixar_playlist(e)
            else:
                func_prosseguir(e)

        def func_prosseguir(e):
            global url_glb
            url_glb=url.value
            yout_inf()
            process_baix(e)

        header=Container(
            content=(Text('YouTube Video Download')),
            alignment=alignment.center,
            width=1000,
            height=50,
            bgcolor=Colors.RED_900,
            border_radius=border_radius.all(5),
            padding=5)

        url=TextField(
            label='Digite a URL',
            filled=True,
            hint_text='https://www.youtube.com/',
            border_radius=border_radius.all(5),
            icon=Icons.SEARCH,
            on_change=desb,
            border_color=Colors.WHITE,
            label_style=TextStyle(
            color = Colors.WHITE))

        Voltar=Button(
                text='Voltar',
                icon=Icons.ARROW_BACK,
                icon_color=Colors.WHITE,
                color=Colors.WHITE,
                on_click=Menu)

        Prosseguir=Button(
                text='Prosseguir',
                icon=Icons.ARROW_FORWARD_SHARP,
                color=Colors.WHITE,
                disabled=True,
                icon_color=Colors.WHITE,
                on_click=func_def)

        Botoes=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,controls=[
            Voltar,
            Prosseguir,
            ])

        col=Column(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            height=100,
            controls=[header,url])

        hub=Column(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            height=147,
            controls=[col,Botoes])

        janela.add(hub) #Adicionar itens principais

    def baixar_playlist(e): #Terceira tela (Download de playlist)
        pass

    def inicio(): #Primeira tela
        
        def esc_vid(e):
            global aux
            aux=1
            process_url(e)
        
        def esc_mus(e):
            global aux
            aux=2
            process_url(e)

        def esc_play(e):
            global aux
            aux=3
            process_url(e)

        janela.window.width = 480
        janela.window.height = 290
        janela.window.resizable = False
        janela.horizontal_alignment = 'center'
        VerticalAlignment.CENTER
        
        itens=list()

        header=Container(
        content=(Text('YouTube Video Download')),
        alignment=alignment.center,
        width=1000,
        height=50,
        bgcolor=Colors.RED_900,
        border_radius=border_radius.all(5),
        padding=5
        )

        itens.append(Container( #Container de baixar vídeo
        content=Row(alignment='spaceBetween',
                controls=[Text('1 -> BAIXAR VÍDEO NO YOUTUBE.',color='black'),
            IconButton(
                icon=Icons.ARROW_RIGHT_ALT,
                icon_color='black',
                hover_color=Colors.WHITE,
                highlight_color=Colors.WHITE,
                on_click=esc_vid
            )]),
        alignment=Alignment(-0.99, -0.1),
        width=1000,
        height=50,
        bgcolor=Colors.WHITE,
        border_radius=border_radius.all(5),
        padding=5
        ))

        itens.append(Container( #Container de baixar música
        content=Row(alignment='spaceBetween',
                controls=[Text('2 -> BAIXAR MÚSICA NO YOUTUBE.',color='black'),
            IconButton(
                icon=Icons.ARROW_RIGHT_ALT,
                icon_color='black',
                hover_color=Colors.WHITE,
                highlight_color=Colors.WHITE,
                on_click=esc_mus
            )]),
        alignment=Alignment(-0.99, -0.1),
        width=1000,
        height=50,
        bgcolor=Colors.WHITE,
        border_radius=border_radius.all(5),
        padding=5
        ))

        itens.append(Container( #Container de baixar playlist
        content=Row(alignment='spaceBetween',
                controls=[Text('3 -> BAIXAR PLAYLIST NO YOUTUBE.',color='black'),
            IconButton(
                icon=Icons.ARROW_RIGHT_ALT,
                icon_color='black',
                hover_color=Colors.WHITE,
                highlight_color=Colors.WHITE,
                on_click=esc_play
            )]),
        alignment=Alignment(-0.99, -0.1),
        width=1000,
        height=50,
        bgcolor=Colors.WHITE,
        border_radius=border_radius.all(5),
        padding=5
        ))

        col = Column(controls=itens)
        janela.add(header,col)

    inicio()

app(gui)
