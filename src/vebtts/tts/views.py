from django.shortcuts import render
from .models import Txt
from .forms import TxtForm
from .programs import tts


# Загрузка страницы home
def index(request):
    form = TxtForm()

    context = {'form': form}
    return render(request, './tts/home.html', context)


# Загрузка страницы down_audio
def down_audio(request):
    # получение post запроса с данными для БД
    if request.method == 'POST':
        form = TxtForm(request.POST)
        if form.is_valid():
            form.save()

    # Загрузка последней информации из БД
    text_form = ''
    if Txt.objects.all():
        text_form = str(Txt.objects.all().last())

    tts(text_form)

    context = {"text": text_form, 'form': TxtForm()}
    return render(request, './tts/down_audio.html', context)
