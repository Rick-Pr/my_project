# Сайт для синтеза речи из текста


## Данный проект позволит переводить текстовую информацию в аудио формат, прослушать и скачать.
## Основан на модуле tts [cilero](https://silero.ai/tag/text-to-speech/)

##Инструкция по установке и запуску
Шаг 1. Clone this repository:
```
git clone
```

Шаг 2. Переход в папку проекта .\my_project\src\vebtts:
```
В терминале cd К пути где находится my_project добавить \my_project\src\vebtts 
Например cd C:\my_project\src\vebtts
```
Шаг 3. Установка модулей:
```
pip install -r requirements.txt
```
В случае ошибки:
```
python py -m pip install --upgrade pip
```

Шаг 4. Сделать миграции:
```
py manage.py makemigrations
```
```
py manage.py migrate Txt
```

Шаг 5. Запустить локальный сервер:
```
py manage.py runserver
```
## Доступен только русский язык, символы и иностранные слова будут пропущены.
## Для внимательного изучения и настройки tts обращайтесь к официальному источнику: [silero colab](https://colab.research.google.com/github/snakers4/silero-models/blob/master/examples_tts.ipynb)

