from .models import Txt
from django.forms import ModelForm, Textarea


# Форма для ввода текста со страницы home
class TxtForm(ModelForm):
    class Meta:
        model = Txt
        fields = ['name']
        widgets = {
            'name': Textarea(attrs={
                'class': 'text_control',
                'name': "text",
                'placeholder': 'Введите ваш текст:'
            })}
