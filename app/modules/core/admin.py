from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline, TranslationTabularInline
from .models import (
    AffiliatedPersonsList,
    CorporateEvent,
    FinancialReport,
    OrgChart,
    OrgUnit,
    PrivacyPolicy,
    PrivacyPolicySection,
)


@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('year', 'report_type', 'uploaded_at')
    list_filter = ('year', 'report_type')


@admin.register(AffiliatedPersonsList)
class AffiliatedPersonsListAdmin(admin.ModelAdmin):
    list_display = ('year', 'quarter', 'uploaded_at')
    list_filter = ('year',)


@admin.register(CorporateEvent)
class CorporateEventAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'month', 'year')
    list_filter = ('year',)


@admin.register(OrgChart)
class OrgChartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'updated_at')

    def has_add_permission(self, request):
        return not OrgChart.objects.exists()


class OrgUnitInline(TranslationTabularInline):
    model = OrgUnit
    fk_name = 'parent'
    extra = 1
    fields = ('name', 'count', 'order')


@admin.register(OrgUnit)
class OrgUnitAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'count', 'parent', 'order')
    list_filter = ('parent',)
    list_editable = ('order',)
    inlines = [OrgUnitInline]


class PrivacyPolicySectionInline(TranslationStackedInline):
    model = PrivacyPolicySection
    extra = 1
    fields = ('title', 'content', 'list_items', 'order')


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(TabbedTranslationAdmin):
    list_display = ('document_title', 'updated_date', 'contact_email')
    inlines = [PrivacyPolicySectionInline]

    def has_add_permission(self, request):
        return not PrivacyPolicy.objects.exists()


@admin.register(PrivacyPolicySection)
class PrivacyPolicySectionAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'policy', 'order')
    list_filter = ('policy',)
    list_editable = ('order',)
    search_fields = ('title', 'content', 'list_items')
