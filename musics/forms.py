from django import forms

from musics.models import Music


class MusicCreateForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name', 'year', 'file']


class MusicUpdateForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name', 'year', 'file']
