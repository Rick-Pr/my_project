from .models import Txt
from django.forms import ModelForm, TextInput, Textarea

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