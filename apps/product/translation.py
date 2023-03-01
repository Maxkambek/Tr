from .models import Product, Category, Subcategory
from modeltranslation.translator import TranslationOptions, register
from modeltranslation.admin import TranslationAdmin


class CustomTranslationsAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(Product)
class PostTranslations(TranslationOptions):
    fields = ('name', 'description', 'characteristic', 'made_in', 'type_cash')


@register(Category)
class PostTranslations(TranslationOptions):
    fields = ('name',)


@register(Subcategory)
class PostTranslations(TranslationOptions):
    fields = ('name',)
