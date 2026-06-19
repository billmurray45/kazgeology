from django.db import migrations, models


def seed_history_events(apps, schema_editor):
    AboutHistoryEvent = apps.get_model('about', 'AboutHistoryEvent')

    events = [
        {
            'year': 2011,
            'date_label': '21 июня 2011',
            'title': 'Основание компании',
            'description': (
                'Постановлением Правительства РК №684 от 21 июня 2011 года АО «Казгеология» '
                'создано как высокотехнологичная геологоразведочная компания Республики Казахстан.'
            ),
            'document_reference': 'Постановление Правительства РК №684',
            'is_featured': True,
            'order': 1,
        },
        {
            'year': 2021,
            'date_label': '30 декабря 2021',
            'title': 'Переход под управление Самрук-Қазына',
            'description': (
                'Постановлением Правительства РК №971 от 30 декабря 2021 года принято решение '
                'о передаче акций компании в АО «Фонд национального благосостояния «Самрук-Қазына».'
            ),
            'document_reference': 'Постановление Правительства РК №971',
            'order': 2,
        },
        {
            'year': 2023,
            'date_label': '8 сентября 2023',
            'title': 'Передача 100% акций в Самрук-Қазына',
            'description': (
                'Приказом Председателя Комитета государственного имущества и приватизации '
                'Министерства финансов РК №650 от 8 сентября 2023 года осуществлена передача '
                '100% акций компании в собственность АО «ФНБ «Самрук-Қазына».'
            ),
            'document_reference': 'Приказ Председателя КГИП МФ РК №650',
            'order': 3,
        },
        {
            'year': 2023,
            'date_label': '14 сентября 2023',
            'title': 'Передача голосующих акций в Тау-Кен Самрук',
            'description': (
                'На основании договора №1707-И от 14 сентября 2023 года произведена передача '
                '100% голосующих акций АО «Казгеология» от АО «ФНБ «Самрук-Қазына» '
                'в АО «НГК «Тау-Кен Самрук».'
            ),
            'document_reference': 'Договор №1707-И',
            'order': 4,
        },
    ]

    for event in events:
        AboutHistoryEvent.objects.get_or_create(
            title=event['title'],
            date_label=event['date_label'],
            defaults=event,
        )


def remove_history_events(apps, schema_editor):
    AboutHistoryEvent = apps.get_model('about', 'AboutHistoryEvent')
    AboutHistoryEvent.objects.filter(
        title__in=[
            'Основание компании',
            'Переход под управление Самрук-Қазына',
            'Передача 100% акций в Самрук-Қазына',
            'Передача голосующих акций в Тау-Кен Самрук',
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_seed_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutHistoryEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(verbose_name='Год')),
                ('date_label', models.CharField(max_length=100, verbose_name='Дата')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок события')),
                ('description', models.TextField(verbose_name='Описание события')),
                ('document_reference', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на документ')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Выделенная карточка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на сайте')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Событие истории компании',
                'verbose_name_plural': 'История компании',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.RunPython(seed_history_events, remove_history_events),
    ]
