from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','annotation', 'text', 'date']

        widgets = {
            'title' : TextInput(attrs={
                'class':  "form-control",
                'placeholder':"Название статьи"
            }),
            'annotation' : TextInput(attrs={
                'class': "form-control",
                'placeholder': "Аннотации"

            }),
            'date' : DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Дата публикации'
            }),
            'text' : Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Введите текст'
            }),

        }
