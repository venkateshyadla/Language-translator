from django import forms
from .models import Translation

class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ['source_language', 'target_language', 'text_to_translate']
