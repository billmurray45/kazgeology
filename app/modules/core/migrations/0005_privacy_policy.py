from django.db import migrations, models
import django.db.models.deletion


def seed_privacy_policy(apps, schema_editor):
    PrivacyPolicy = apps.get_model('core', 'PrivacyPolicy')
    PrivacyPolicySection = apps.get_model('core', 'PrivacyPolicySection')

    policy, _ = PrivacyPolicy.objects.get_or_create(
        document_title='Политика конфиденциальности',
        defaults={
            'hero_label': 'АО «Казгеология»',
            'hero_title': 'ПОЛИТИКА\nКОНФИДЕНЦИАЛЬНОСТИ',
            'hero_subtitle': 'Порядок обработки и защиты персональных данных пользователей сайта.',
            'updated_date': '28 мая 2026',
            'contact_email': 'info@kazgeology.kz',
            'intro_text': (
                'Настоящая Политика конфиденциальности определяет порядок сбора, хранения, '
                'использования и защиты персональных данных пользователей сайта АО «Казгеология».'
            ),
        },
    )

    sections = [
        {
            'title': '1. Общие положения',
            'content': (
                'АО «Казгеология» уважает право пользователей на конфиденциальность и принимает '
                'необходимые организационные и технические меры для защиты предоставленной информации.\n\n'
                'Используя сайт, пользователь подтверждает ознакомление с настоящей Политикой и '
                'соглашается с условиями обработки данных в пределах, необходимых для работы сайта '
                'и обратной связи.'
            ),
            'order': 1,
        },
        {
            'title': '2. Какие данные могут обрабатываться',
            'content': 'Компания может обрабатывать следующие сведения:',
            'list_items': (
                'имя, адрес электронной почты, номер телефона и текст обращения;\n'
                'технические данные: IP-адрес, тип браузера, дата и время посещения;\n'
                'информацию, которую пользователь добровольно передает через формы сайта.'
            ),
            'order': 2,
        },
        {
            'title': '3. Цели обработки данных',
            'content': 'Персональные данные используются для:',
            'list_items': (
                'обработки обращений и предоставления ответа пользователю;\n'
                'обеспечения корректной и безопасной работы сайта;\n'
                'выполнения требований законодательства Республики Казахстан;\n'
                'улучшения качества информационных материалов и сервисов сайта.'
            ),
            'order': 3,
        },
        {
            'title': '4. Передача данных третьим лицам',
            'content': (
                'Компания не передает персональные данные третьим лицам без согласия пользователя, '
                'за исключением случаев, предусмотренных законодательством, либо когда такая передача '
                'необходима для обработки обращения пользователя.'
            ),
            'order': 4,
        },
        {
            'title': '5. Хранение и защита данных',
            'content': (
                'Данные хранятся в течение срока, необходимого для достижения целей обработки, если '
                'иной срок не установлен законодательством. Компания применяет разумные меры защиты '
                'от несанкционированного доступа, изменения, раскрытия или уничтожения информации.'
            ),
            'order': 5,
        },
        {
            'title': '6. Права пользователя',
            'content': 'Пользователь вправе запросить информацию об обработке своих данных, а также обратиться с просьбой:',
            'list_items': (
                'уточнить или обновить персональные данные;\n'
                'прекратить обработку данных, если для этого есть законные основания;\n'
                'получить разъяснение по вопросам защиты персональных данных.'
            ),
            'order': 6,
        },
        {
            'title': '7. Изменение политики',
            'content': (
                'Компания может обновлять настоящую Политику. Актуальная редакция размещается на '
                'этой странице и применяется с момента публикации, если в тексте не указано иное.'
            ),
            'order': 7,
        },
    ]

    for section in sections:
        PrivacyPolicySection.objects.get_or_create(
            policy=policy,
            title=section['title'],
            defaults={
                'content': section['content'],
                'list_items': section.get('list_items', ''),
                'order': section['order'],
            },
        )


def remove_privacy_policy(apps, schema_editor):
    PrivacyPolicy = apps.get_model('core', 'PrivacyPolicy')
    PrivacyPolicy.objects.filter(document_title='Политика конфиденциальности').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_orgchart'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_label', models.CharField(default='АО «Казгеология»', max_length=100, verbose_name='Метка в шапке')),
                ('hero_title', models.CharField(max_length=255, verbose_name='Заголовок страницы')),
                ('hero_subtitle', models.CharField(max_length=255, verbose_name='Подзаголовок страницы')),
                ('document_title', models.CharField(max_length=255, verbose_name='Название документа')),
                ('updated_date', models.CharField(max_length=100, verbose_name='Дата обновления')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Контактный email')),
                ('intro_text', models.TextField(verbose_name='Вводный текст')),
            ],
            options={
                'verbose_name': 'Политика конфиденциальности',
                'verbose_name_plural': 'Политика конфиденциальности',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок секции')),
                ('content', models.TextField(help_text='Для нескольких абзацев разделяйте текст пустой строкой.', verbose_name='Текст секции')),
                ('list_items', models.TextField(blank=True, help_text='Каждый пункт с новой строки.', verbose_name='Пункты списка')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='core.privacypolicy', verbose_name='Политика')),
            ],
            options={
                'verbose_name': 'Секция политики конфиденциальности',
                'verbose_name_plural': 'Секции политики конфиденциальности',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.RunPython(seed_privacy_policy, remove_privacy_policy),
    ]
