from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from .models import BoardCommittee, BoardCommitteeMember, BoardMember, BoardSecretary


@admin.register(BoardMember)
class BoardMemberAdmin(TabbedTranslationAdmin):
    list_display = ('full_name', 'role', 'photo_preview', 'is_chair', 'is_active', 'order')
    list_editable = ('is_chair', 'is_active', 'order')
    list_filter = ('is_chair', 'is_active')
    search_fields = ('full_name', 'role')
    ordering = ('order', 'id')
    readonly_fields = ('photo_preview',)

    @admin.display(description='Фото')
    def photo_preview(self, obj):
        if not obj.photo:
            return '—'

        return format_html(
            '<img src="{}" style="width: 72px; height: 96px; object-fit: cover; border-radius: 4px;" />',
            obj.photo_url,
        )


@admin.register(BoardSecretary)
class BoardSecretaryAdmin(TabbedTranslationAdmin):
    list_display = ('label', 'full_name', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('label', 'full_name')

    def has_add_permission(self, request):
        return not BoardSecretary.objects.exists()


class BoardCommitteeMemberInline(TranslationTabularInline):
    model = BoardCommitteeMember
    extra = 1
    fields = ('full_name', 'note', 'role_label', 'is_chair', 'is_active', 'order')


@admin.register(BoardCommittee)
class BoardCommitteeAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'count_label', 'icon_class', 'is_active', 'order')
    list_editable = ('icon_class', 'is_active', 'order')
    search_fields = ('title',)
    ordering = ('order', 'id')
    inlines = [BoardCommitteeMemberInline]


@admin.register(BoardCommitteeMember)
class BoardCommitteeMemberAdmin(TabbedTranslationAdmin):
    list_display = ('full_name', 'committee', 'role_label', 'note', 'is_chair', 'is_active', 'order')
    list_editable = ('is_chair', 'is_active', 'order')
    list_filter = ('committee', 'is_chair', 'is_active')
    search_fields = ('full_name', 'note', 'committee__title')
    ordering = ('committee', 'order', 'id')
