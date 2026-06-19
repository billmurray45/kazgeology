from django.contrib import admin
from .models import AboutHistoryEvent, AboutSection, AboutStatistic


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_stat_value', 'main_stat_description')

    def has_add_permission(self, request):
        # Allow adding a record only if none exist (singleton pattern)
        return not AboutSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion to keep the homepage config safe
        return False


@admin.register(AboutStatistic)
class AboutStatisticAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'description', 'order')
    list_editable = ('order',)
    ordering = ('order', 'id')


@admin.register(AboutHistoryEvent)
class AboutHistoryEventAdmin(admin.ModelAdmin):
    list_display = ('year', 'date_label', 'title', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('year', 'is_featured', 'is_active')
    search_fields = ('title', 'description', 'document_reference')
    ordering = ('order', 'id')
