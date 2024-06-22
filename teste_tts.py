
# from script import load_model,Path,Data,this_dir,params

# import html
# import json
# import os
# import random
# import time
# from pathlib import Path
from datetime import datetime
import re

# try:
#   import gradio as gr
# except:
# #   pip install gradio
#   import gradio as gr
try:
  import torch
except:
#   pip install torch
  import torch
import flet as ft
from TTS.api import TTS
# from TTS.utils.synthesizer import Synthesizer
params = {
    "activate": True,
    "autoplay": True,
    "show_text": False,
    "remove_trailing_dots": True,
    "voice": "ivan lima3.wav",
    "language": "Portuguese",
    "model_name": "tts_models/multilingual/multi-dataset/xtts_v2",
    "device": "cuda" if torch.cuda.is_available() else "cpu"
}

def Data():
    current_time = datetime.now()
    formatted_time = current_time.strftime('%d-%m-%Y-%H-%M-%S')
    return formatted_time

def load_model():
    model = TTS(params["model_name"]).to(params["device"])
    return model


# texto = 'a chave para uma vida bem sucedida. '

def voice_preview2(string):
    output_file = f"voice_preview_{Data()}.wav"
    model = load_model()
    model.tts_to_file(
        text=string,
        file_path=output_file,
        speaker_wav=["ivan lima3.wav"],
        language="pt"
    )
    print(f'Áudio gerado....')
    return f'<audio src="{output_file}" controls autoplay></audio>'






def main(page: ft.Page):
    page.window_width = 300  # Define a largura da janela como 800 pixels
    page.window_height = 300  # 
    bgcolor = 'white'
    cor_texto = 'black'
    page.theme = ft.Theme(
        color_scheme_seed = 'white',
        color_scheme = ft.ColorScheme(background = 'white'),
        primary_color = 'red',
        primary_color_dark = 'red',
        primary_text_theme = ft.TextStyle(color = cor_texto),
        dialog_theme = ft.DialogTheme(
            bgcolor = bgcolor,
            title_text_style = ft.TextStyle(color = cor_texto),
            content_text_style = ft.TextStyle(color = cor_texto),
            alignment = ft.Alignment(0, 0),
            actions_padding = 2,
       )
        
        )
    COR1 = 'white,0.5'
    COR2 = 'black'
    COR3 = 'white'
    page.bgcolor = '#282a36'
    page.title = "Falar Texto e Clonar Voz"
    # page.theme_mode = ft.ThemeMode.DARK
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

 

    def Get_links(e):
        url_pattern = r'https?://[^\s]+'
        texto.value = re.findall(url_pattern, e.control.value)
        



    texto = ft.TextField(label = 'texto',hint_text="Insira o texto aqui", on_change=Get_links) #, border_color = 'white,0.8'
    botao_executar = ft.ElevatedButton("Executar", on_click=lambda e: voice_preview2(texto.value))
    # select_button = SaveSelectFile2('path', json='config_baixar_youtube')
    # mp3 = ft.Checkbox(label = 'Converter para mp3?', value = state_select, on_change=Chenge_select, )
    output = ft.Text("")




    def Output(texto):
       output.value += f'{texto}\n'
       page.update()


 


    page.add(
        ft.Column(
            [
                # ft.Text("Baixar vídeos do Youtube", style=ft.TextStyle(size=24)),
                # url_field,
                texto,
                botao_executar,                
                # ft.Row([download_button,mp3]),
                ft.Container(ft.Column([output],auto_scroll = True, scroll=ft.ScrollMode.ADAPTIVE, height=90, width=page.window_height),bgcolor=f'red,0.1')
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )




ft.app(main, 

)