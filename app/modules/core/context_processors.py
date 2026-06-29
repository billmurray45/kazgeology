LANG_LABELS = [
    ('ru', 'РУС'),
    ('kk', 'ҚАЗ'),
    ('en', 'ENG'),
]


def lang_labels(request):
    """Expose short language labels for the header switcher."""
    return {'lang_labels': LANG_LABELS}
