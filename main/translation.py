from .models import New
from modeltranslation.translator import TranslationOptions, register


@register(New)
class NewsTranslationOptions(TranslationOptions):
      fields = ('title', 'body')
