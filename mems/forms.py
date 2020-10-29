from django import forms
from django.core.exceptions import ValidationError
from .models import MemPost


class MemForm(forms.Form):
    title = forms.CharField(label='Название', max_length=150)
    slug = forms.CharField(label='url', max_length=150)
    body = forms.CharField(label='Текст', max_length=300, widget=forms.Textarea)
    image = forms.ImageField()

    def clean_slug(self):

        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Нельзя создать такой url.')
        if MemPost.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Такой url уже есть.')
        return new_slug

    def save(self):
        new_mem = MemPost.objects.create(title=self.cleaned_data['title'],
                                         slug=self.cleaned_data['slug'],
                                         body=self.cleaned_data['body'],
                                         image=self.cleaned_data['image'],
                                         )
        return new_mem