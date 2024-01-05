from pydub import AudioSegment
import torch
import shutil
import soundfile as sf
from os import path
import os


def tts(text_form):
    def va_speak(what: str):
        name = 'small_fast'  # 'large_fast', 'small_fast', 'small_slow'
        language = 'ru'  # язык озвучки
        model_id = 'v4_ru'  # версия модуля
        sample_rate = 48000  # частота аудио 48000
        speaker = 'baya'  # голоса: aidar, baya, xenia, random
        put_accent = True
        put_yo = True
        device = torch.device('cpu')  # cpu или gpu

        # Установка количество потоков для обработки
        torch.set_num_threads(4)

        # Получение и обработка модели
        torch.hub.download_url_to_file('https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml',
                                       'latest_silero_models.yml',
                                       progress=False)
        model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                  model='silero_tts',
                                  language=language,
                                  speaker=model_id,
                                  name=name)
        model.to(device)
        # Подключение и загрузка модели
        audio = model.apply_tts(text=what + "..",
                                speaker=speaker,
                                sample_rate=sample_rate,
                                put_accent=put_accent,
                                put_yo=put_yo)

        # Сохранение части записи
        output_file = 'output.wav'
        sf.write(output_file, audio, sample_rate)

    # Разбиение текста на части для буфера PyTorch
    def preprocessing_text(text):
        t = []
        while len(text) > 800:
            t.append(text[:800])
            text = text[800:]
        t.append(text)
        return t

    # Получение текста и создание цельного аудио
    def main(txt):
        # Синтез речи по 800 знаков и совмещение в один аудио файл
        num = 1
        for text in preprocessing_text(txt):
            va_speak(text)
            file1 = 'audio_file.wav'
            file2 = 'output.wav'
            if num == 1:
                print(1)
                print(os.getcwd())
                file1 = './src/vebtts/tts/static/tts/files/silent.wav'

            song1 = AudioSegment.from_wav(f"{file1}", '')
            song2 = AudioSegment.from_wav(f"{file2}")
            s3 = song1 + song2
            s3.export("./audio_file.wav", format="wav")
            num += 1
        output_file = 'audio_file.wav'

        # перенос готового аудио в .\files и удаление буферного файла
        source_path = str(os.getcwd()) + '\\' + output_file
        source_path = os.path.normpath(source_path)
        print(source_path)
        destination_path = str(os.getcwd()) + '\\src\\vebtts\\tts\\static\\tts\\files\\audio_file.wav'
        destination_path = os.path.normpath(destination_path)
        if path.exists(source_path):
            print(destination_path)
            shutil.move(source_path, destination_path)

        os.remove('output.wav')

    # удаление предыдущей записи tts
    destination_path = str(os.getcwd()) + '\\src\\vebtts\\tts\\static\\tts\\files\\audio_file.wav'
    destination_path = os.path.normpath(destination_path)
    if path.exists(destination_path):
        os.remove(destination_path)

    # Проверка введённого значения
    try:
        main(text_form)
    except ValueError:
        pass
