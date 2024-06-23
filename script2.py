import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
  import gradio as gr
except:
    install(gradio) # type: ignore
    import gradio as gr
try:
  import torch
except:
    install(torch)
    import torch


try:
  from TTS.api import TTS
  from TTS.utils.synthesizer import Synthesizer
except:
  install(TTS)
  from TTS.api import TTS
  from TTS.utils.synthesizer import Synthesizer

# from modules import chat, shared, ui_chat
# from modules.ui import create_refresh_button
# from modules.utils import gradio

os.environ["COQUI_TOS_AGREED"] = "1"

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

this_dir = str(Path(__file__).parent.resolve())
# this_dir = '/content'
model = None


def load_model():
    model = TTS(params["model_name"]).to(params["device"])
    return model






def Data():
    current_time = datetime.now()
    formatted_time = current_time.strftime('%d-%m-%Y-%H-%M-%S')
    return formatted_time

def new_split_into_sentences(self, text):
    sentences = self.seg.segment(text)
    if params['remove_trailing_dots']:
        sentences_without_dots = []
        for sentence in sentences:
            if sentence.endswith('.') and not sentence.endswith('...'):
                sentence = sentence[:-1]

            sentences_without_dots.append(sentence)

        return sentences_without_dots
    else:
        return sentences


Synthesizer.split_into_sentences = new_split_into_sentences

model = load_model()

def voice_preview2(string, directory, velocidade = 1.6):
  output_file = os.path.join(directory, f'voice_preview_{Data()}.wav')
  model.tts_to_file(
      text=string,
      file_path=output_file,
      speed = velocidade,
      speaker_wav=[f"{this_dir}/{params['voice']}"],
      language="pt"
  )
  print(f'Áudio gerado....')
  # return f'<audio src="file/{output_file.as_posix()}?{int(time.time())}" controls autoplay></audio>'

