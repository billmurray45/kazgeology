from modeltranslation.translator import register, TranslationOptions

from .models import CorporateEvent, OrgUnit, PrivacyPolicy, PrivacyPolicySection


@register(CorporateEvent)
class CorporateEventTR(TranslationOptions):
    fields = ('title',)


@register(OrgUnit)
class OrgUnitTR(TranslationOptions):
    fields = ('name',)


@register(PrivacyPolicy)
class PrivacyPolicyTR(TranslationOptions):
    fields = ('hero_label', 'hero_title', 'hero_subtitle', 'document_title', 'updated_date', 'intro_text')


@register(PrivacyPolicySection)
class PrivacyPolicySectionTR(TranslationOptions):
    fields = ('title', 'content', 'list_items')
