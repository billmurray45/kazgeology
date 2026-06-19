from django.db import migrations, models
import django.db.models.deletion


def seed_committee_data(apps, schema_editor):
    BoardCommittee = apps.get_model('board', 'BoardCommittee')
    BoardCommitteeMember = apps.get_model('board', 'BoardCommitteeMember')

    committees = [
        {
            'title': 'Комитет по стратегическому планированию, инвестициям и устойчивому развитию',
            'count_label': '4 человека',
            'icon_class': 'fa-solid fa-chart-line',
            'order': 1,
            'members': [
                {
                    'full_name': 'Перзадаев М.А.',
                    'note': 'независимый директор',
                    'role_label': 'Председатель',
                    'is_chair': True,
                    'order': 1,
                },
                {
                    'full_name': 'Бергенев А.С.',
                    'note': 'независимый директор',
                    'order': 2,
                },
                {
                    'full_name': 'Жумагулов Р.Б.',
                    'note': 'представитель ЕА',
                    'order': 3,
                },
            ],
        },
        {
            'title': 'Комитет по кадрам, вознаграждениям и социальным вопросам',
            'count_label': '4 человека',
            'icon_class': 'fa-solid fa-users',
            'order': 2,
            'members': [
                {
                    'full_name': 'Жумагулов Р.Б.',
                    'note': 'представитель ЕА',
                    'role_label': 'Председатель',
                    'is_chair': True,
                    'order': 1,
                },
                {
                    'full_name': 'Перзадаев М.А.',
                    'note': 'независимый директор',
                    'order': 2,
                },
                {
                    'full_name': 'Бергенев А.С.',
                    'note': 'независимый директор',
                    'order': 3,
                },
            ],
        },
        {
            'title': 'Комитет по аудиту',
            'count_label': '4 человека',
            'icon_class': 'fa-solid fa-magnifying-glass-chart',
            'order': 3,
            'members': [
                {
                    'full_name': 'Бергенев А.С.',
                    'note': 'независимый директор',
                    'role_label': 'Председатель',
                    'is_chair': True,
                    'order': 1,
                },
                {
                    'full_name': 'Перзадаев М.А.',
                    'note': 'независимый директор',
                    'order': 2,
                },
                {
                    'full_name': 'Жумагулов Р.Б.',
                    'note': 'представитель ЕА',
                    'order': 3,
                },
            ],
        },
    ]

    for item in committees:
        members = item.pop('members')
        committee, _ = BoardCommittee.objects.get_or_create(
            title=item['title'],
            defaults=item,
        )
        for member in members:
            BoardCommitteeMember.objects.get_or_create(
                committee=committee,
                full_name=member['full_name'],
                defaults=member,
            )


def remove_committee_data(apps, schema_editor):
    BoardCommittee = apps.get_model('board', 'BoardCommittee')

    BoardCommittee.objects.filter(
        title__in=[
            'Комитет по стратегическому планированию, инвестициям и устойчивому развитию',
            'Комитет по кадрам, вознаграждениям и социальным вопросам',
            'Комитет по аудиту',
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_seed_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название комитета')),
                ('count_label', models.CharField(max_length=50, verbose_name='Подпись количества')),
                ('icon_class', models.CharField(default='fa-solid fa-users', help_text='Например: fa-solid fa-chart-line', max_length=100, verbose_name='CSS-класс иконки')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на сайте')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Комитет Совета директоров',
                'verbose_name_plural': 'Комитеты Совета директоров',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='BoardCommitteeMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('note', models.CharField(blank=True, max_length=255, verbose_name='Примечание')),
                ('role_label', models.CharField(blank=True, max_length=50, verbose_name='Метка роли')),
                ('is_chair', models.BooleanField(default=False, verbose_name='Председатель')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на сайте')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='board.boardcommittee', verbose_name='Комитет')),
            ],
            options={
                'verbose_name': 'Участник комитета',
                'verbose_name_plural': 'Участники комитетов',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.RunPython(seed_committee_data, remove_committee_data),
    ]
