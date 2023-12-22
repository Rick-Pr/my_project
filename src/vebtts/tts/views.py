from django.shortcuts import render
from .models import Txt
from .forms import TxtForm
from pydub import AudioSegment
import torch
import shutil
import soundfile as sf

from os import path
import os


def index(request):
    form = TxtForm()

    context = {'form': form}
    return render(request, './tts/home.html', context)


def down_audio(request):
    if request.method == 'POST':
        form = TxtForm(request.POST)
        if form.is_valid():
            form.save()

    text_form = ''
    if Txt.objects.all():
        text_form = str(Txt.objects.all().last())

    # os.remove('/static/tts/files/audio_file.wav')
    destination_path = str(os.getcwd()) + '\\tts\\static\\tts\\files\\audio_file.wav'
    destination_path = os.path.normpath(destination_path)
    if path.exists(destination_path):
        os.remove(destination_path)

    try:
        main(text_form)
    except ValueError:
        pass

    form = TxtForm()
    context = {"text": text_form, 'form': form}
    return render(request, './tts/down_audio.html', context)


def va_speak(what: str):
    name = 'small_fast'  # 'large_fast', 'small_fast', 'small_slow'
    language = 'ru'  # язык озвучки
    model_id = 'v4_ru'  # версия модуля
    sample_rate = 48000  # частота аудио 48000
    speaker = 'baya'  # голоса: aidar, baya, xenia, random
    put_accent = True
    put_yo = True
    device = torch.device('cpu')  # cpu или gpu

    torch.set_num_threads(4)
    torch.hub.download_url_to_file('https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml',
                                   'latest_silero_models.yml',
                                   progress=False)
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id,
                              name=name)
    model.to(device)

    audio = model.apply_tts(text=what + "..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    output_file = 'output.wav'
    sf.write(output_file, audio, sample_rate)


def preprocessing_text(text):
    t = []
    while len(text) > 800:
        t.append(text[:800])
        text = text[800:]
    t.append(text)
    return t


def main(txt):
    set_of_texts = preprocessing_text(txt)

    num = 1
    for text in set_of_texts:
        va_speak(text)
        file1 = 'audio_file.wav'
        file2 = 'output.wav'
        if num == 1:
            file1 = './tts/static/tts/files/silent.wav'

        song1 = AudioSegment.from_wav(f"{file1}", '')
        song2 = AudioSegment.from_wav(f"{file2}")
        s3 = song1 + song2
        s3.export("./audio_file.wav", format="wav")
        num += 1

    output_file = 'audio_file.wav'

    # Установить имя файла с путем
    source_path = str(os.getcwd()) + '\\' + output_file
    source_path = os.path.normpath(source_path)
    if path.exists(source_path):
        destination_path = str(os.getcwd()) + '\\tts\\static\\tts\\files\\' + output_file
        destination_path = os.path.normpath(destination_path)
        shutil.move(source_path, destination_path)

    os.remove('output.wav')
