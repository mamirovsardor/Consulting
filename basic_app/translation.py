from modeltranslation.translator import register, TranslationOptions
from basic_app.models import *


@register(Services)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Facts)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'number')
    
@register(Team)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'prof',"des")    
    
    
@register(Price)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'price',"month","addition1", "addition2", "addition3", "addition4", "addition5") 
    
    
@register(Blog)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'date',"des") 
    
@register(Testimonial)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', "des") 
    
@register(Contact)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'email',"phone","message")