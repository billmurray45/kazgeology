from django.db import migrations, models
import modules.board.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardSecretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, verbose_name='Должность')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на сайте')),
            ],
            options={
                'verbose_name': 'Корпоративный секретарь',
                'verbose_name_plural': 'Корпоративный секретарь',
            },
        ),
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('role', models.CharField(max_length=255, verbose_name='Роль')),
                ('photo', models.ImageField(blank=True, upload_to=modules.board.models.board_member_photo_upload_to, verbose_name='Фото')),
                ('is_chair', models.BooleanField(default=False, verbose_name='Председатель')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на сайте')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Член Совета директоров',
                'verbose_name_plural': 'Члены Совета директоров',
                'ordering': ['order', 'id'],
            },
        ),
    ]
