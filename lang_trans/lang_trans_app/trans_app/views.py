from django.shortcuts import render
from .forms import TranslationForm
from .models import Translation
from indictrans import Transliterator
from googletrans import Translator


def transliterate_to_english(source,text):
    transliterator = Transliterator(source='source', target='english')
    transliterated_text = transliterator.transform(text)
    return transliterated_text

def translate_text(request):
    translation_result = None
    language_choices = [
                ('hi', 'Hindi'),
                ('te', 'Telugu'),
                ('en', 'English'),
                ('ta', 'Tamil'),
                ('kn', 'Kannada'),
                ('bn', 'Bengali'),
                ('mr', 'Marathi'),
                ('ur', 'Urdu'),
                ('gu', 'Gujarati'),
                ('or', 'Odia'),
                ('ml', 'Malayalam'),
                ('pa', 'Punjabi'),
                ('as', 'Assamese'),
                ('kn', 'Kannada'),
                ('mr', 'Marathi'),
                ('ne', 'Nepali'),
            ]
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        try:
            if form.is_valid():
                translation_request = form.save(commit=False)
                translator = Translator()
                translation = translator.translate(translation_request.text_to_translate, 
                                                src=translation_request.source_language,
                                                dest=translation_request.target_language)
                translation_request.translated_text = translation.text
                translation_request.save()
                speech = transliterate_to_english(translation_request.source_language,translation_request.translated_text)
                translation_result = {
                    'source_language': translation_request.source_language,
                    'target_language': translation_request.target_language,
                    'text_to_translate': translation_request.text_to_translate,
                    'translated_text': translation_request.translated_text,
                    'speech':speech,
                }
        except:
            err_msg = "Internet connection required.....!"
            return render(request, 'translate.html', {'form': form,'language_choices':language_choices,'err_msg':err_msg})
    else:
        form = TranslationForm()

    return render(request, 'translate.html', {'form': form, 'translation_result': translation_result,'language_choices':language_choices})