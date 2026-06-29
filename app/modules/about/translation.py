from modeltranslation.translator import register, TranslationOptions

from .models import AboutSection, AboutStatistic, AboutHistoryEvent


@register(AboutSection)
class AboutSectionTR(TranslationOptions):
    fields = ('title', 'description', 'main_stat_description', 'main_stat_value')


@register(AboutStatistic)
class AboutStatisticTR(TranslationOptions):
    fields = ('description', 'value', 'label')


@register(AboutHistoryEvent)
class AboutHistoryEventTR(TranslationOptions):
    fields = ('date_label', 'title', 'description')
