#@title #Instalação
# import html
# import json
# import random

from script2 import Path
import time
import subprocess
import sys

try:
    from google.colab import files # type: ignore
except:
   pass
# import platform
# Get the current platform name
# platform_name = platform.system()

# Print the platform name
# print(f"Current platform: {platform_name}")


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])



try:
  from pydub import AudioSegment
except ImportError:
  install(pydub)# type: ignore
  from pydub import AudioSegment



texto = "" # @param {type:"string"}

velocidade = 1.6 # @param {type:"slider", min:0.5, max:3, step:0.1}
limpar_pasta = True # @param {type:"boolean"}
def split_string_every_n_chars(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

# Exemplo de uso
input_string = texto
n = 200
result = split_string_every_n_chars(input_string, n)

# for segment in result:
#     print(segment)
result2 = split_string_every_n_chars(result, 400)
directory = Path(f'{this_dir}/saida2')
if not os.path.exists(directory):
  # Create the directory
  os.makedirs(directory)
  print(f'criando pasta {directory}')
elif limpar_pasta:
  print(f'Limpando pasta{directory}......')
  for i in os.listdir(directory):
    os.remove(os.path.join(directory, i))



total = len(result)
for i in result:
  total -= 1
  voice_preview2(i)
  print(f'Faltam {total} partes')


l = []
for i in os.listdir(directory):
  if i.endswith(".wav"):
    l.append(i)
m = sorted(l)
audios = [AudioSegment.from_file(os.path.join(directory, i), format="wav") for i in m]

combined = audios[0]
for i in audios[1:]:
  combined += i

time.sleep(5)
# Exporte o resultado
nome_saida = f"audio_combined_{Data()}.mp3"
combined.export(nome_saida, format="mp3")
files.download(nome_saida)


if __name__ == '__main__':
    import flet as ft
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