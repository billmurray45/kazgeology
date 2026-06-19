from django.contrib import admin
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
class CorporateEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'month', 'year')
    list_filter = ('year',)


@admin.register(OrgChart)
class OrgChartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'updated_at')

    def has_add_permission(self, request):
        return not OrgChart.objects.exists()


class OrgUnitInline(admin.TabularInline):
    model = OrgUnit
    fk_name = 'parent'
    extra = 1
    fields = ('name', 'count', 'order')


@admin.register(OrgUnit)
class OrgUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'parent', 'order')
    list_filter = ('parent',)
    list_editable = ('order',)
    inlines = [OrgUnitInline]


class PrivacyPolicySectionInline(admin.StackedInline):
    model = PrivacyPolicySection
    extra = 1
    fields = ('title', 'content', 'list_items', 'order')


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('document_title', 'updated_date', 'contact_email')
    fieldsets = (
        ('Шапка страницы', {
            'fields': ('hero_label', 'hero_title', 'hero_subtitle'),
        }),
        ('Сведения о документе', {
            'fields': ('document_title', 'updated_date', 'contact_email', 'intro_text'),
        }),
    )
    inlines = [PrivacyPolicySectionInline]

    def has_add_permission(self, request):
        return not PrivacyPolicy.objects.exists()


@admin.register(PrivacyPolicySection)
class PrivacyPolicySectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'policy', 'order')
    list_filter = ('policy',)
    list_editable = ('order',)
    search_fields = ('title', 'content', 'list_items')
