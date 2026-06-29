from modeltranslation.translator import register, TranslationOptions

from .models import BoardMember, BoardSecretary, BoardCommittee, BoardCommitteeMember


@register(BoardMember)
class BoardMemberTR(TranslationOptions):
    fields = ('full_name', 'role')


@register(BoardSecretary)
class BoardSecretaryTR(TranslationOptions):
    fields = ('label', 'full_name')


@register(BoardCommittee)
class BoardCommitteeTR(TranslationOptions):
    fields = ('title', 'count_label')


@register(BoardCommitteeMember)
class BoardCommitteeMemberTR(TranslationOptions):
    fields = ('full_name', 'note', 'role_label')
