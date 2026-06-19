from django.db import migrations


def seed_board_data(apps, schema_editor):
    BoardMember = apps.get_model('board', 'BoardMember')
    BoardSecretary = apps.get_model('board', 'BoardSecretary')

    members = [
        {
            'full_name': 'Абсаметов Нариман Малисулы',
            'role': 'Председатель',
            'photo': 'images/staff/absametov.jpg',
            'is_chair': True,
            'order': 1,
        },
        {
            'full_name': 'Жумагулов Руслан Бахытжанович',
            'role': 'Член СД — Представитель Единственного акционера',
            'photo': 'images/staff/zhumagulov.jpg',
            'order': 2,
        },
        {
            'full_name': 'Абуов Даурен Канатович',
            'role': 'Член СД — И.о. Генерального директора',
            'photo': 'images/staff/dauren-kanatovich.jpg',
            'order': 3,
        },
        {
            'full_name': 'Бергенев Адылгазы Садвокасович',
            'role': 'Член СД — Независимый директор',
            'photo': 'images/staff/bergenov.jpeg',
            'order': 4,
        },
        {
            'full_name': 'Перзадаев Мурат Абдукадырович',
            'role': 'Член СД — Независимый директор',
            'photo': 'images/staff/perzadayev.png',
            'order': 5,
        },
    ]

    for member in members:
        BoardMember.objects.get_or_create(
            full_name=member['full_name'],
            defaults=member,
        )

    BoardSecretary.objects.get_or_create(
        full_name='Хабиева Жанель Камалхановна',
        defaults={'label': 'ВРИО Корпоративного секретаря'},
    )


def remove_board_data(apps, schema_editor):
    BoardMember = apps.get_model('board', 'BoardMember')
    BoardSecretary = apps.get_model('board', 'BoardSecretary')

    BoardMember.objects.filter(
        full_name__in=[
            'Абсаметов Нариман Малисулы',
            'Жумагулов Руслан Бахытжанович',
            'Абуов Даурен Канатович',
            'Бергенев Адылгазы Садвокасович',
            'Перзадаев Мурат Абдукадырович',
        ]
    ).delete()
    BoardSecretary.objects.filter(full_name='Хабиева Жанель Камалхановна').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_board_data, remove_board_data),
    ]
