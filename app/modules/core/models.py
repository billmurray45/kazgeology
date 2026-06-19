from django.db import models


class FinancialReport(models.Model):
    REPORT_TYPES = [
        ('consolidated', 'Консолидированная'),
        ('separate', 'Отдельная'),
    ]
    year = models.PositiveIntegerField(verbose_name='Год')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES, verbose_name='Тип')
    file = models.FileField(upload_to='investors/financial/', verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', 'report_type']
        unique_together = ('year', 'report_type')
        verbose_name = 'Финансовая отчётность'
        verbose_name_plural = 'Финансовая отчётность'

    def __str__(self):
        return f'{self.get_report_type_display()} за {self.year} год'


class AffiliatedPersonsList(models.Model):
    QUARTERS = [
        (1, '1 квартал'),
        (2, '2 квартал'),
        (3, '3 квартал'),
        (4, '4 квартал'),
    ]
    year = models.PositiveIntegerField(verbose_name='Год')
    quarter = models.PositiveSmallIntegerField(choices=QUARTERS, verbose_name='Квартал')
    file = models.FileField(upload_to='investors/affiliated/', verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-quarter']
        unique_together = ('year', 'quarter')
        verbose_name = 'Список аффилированных лиц'
        verbose_name_plural = 'Списки аффилированных лиц'

    def __str__(self):
        return f'{self.get_quarter_display()} {self.year}'


class CorporateEvent(models.Model):
    MONTHS = [
        (1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'),
        (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'),
        (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь'),
    ]
    title = models.CharField(max_length=255, verbose_name='Название')
    month = models.PositiveSmallIntegerField(choices=MONTHS, verbose_name='Месяц')
    year = models.PositiveIntegerField(verbose_name='Год')

    class Meta:
        ordering = ['year', 'month']
        verbose_name = 'Корпоративное событие'
        verbose_name_plural = 'Корпоративные события'

    def __str__(self):
        return f'{self.get_month_display()} {self.year} — {self.title}'


class OrgChart(models.Model):
    image = models.ImageField(upload_to='org/', verbose_name='Схема структуры')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Организационная структура'
        verbose_name_plural = 'Организационная структура'

    def __str__(self):
        return 'Организационная структура'


class OrgUnit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    count = models.CharField(max_length=20, blank=True, verbose_name='Кол-во единиц')
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родительский узел',
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Организационная структура'

    def __str__(self):
        return self.name


class PrivacyPolicy(models.Model):
    hero_label = models.CharField(max_length=100, default='АО «Казгеология»', verbose_name='Метка в шапке')
    hero_title = models.CharField(max_length=255, verbose_name='Заголовок страницы')
    hero_subtitle = models.CharField(max_length=255, verbose_name='Подзаголовок страницы')
    document_title = models.CharField(max_length=255, verbose_name='Название документа')
    updated_date = models.CharField(max_length=100, verbose_name='Дата обновления')
    contact_email = models.EmailField(verbose_name='Контактный email')
    intro_text = models.TextField(verbose_name='Вводный текст')

    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'

    def __str__(self):
        return self.document_title


class PrivacyPolicySection(models.Model):
    policy = models.ForeignKey(
        PrivacyPolicy,
        on_delete=models.CASCADE,
        related_name='sections',
        verbose_name='Политика',
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок секции')
    content = models.TextField(
        verbose_name='Текст секции',
        help_text='Для нескольких абзацев разделяйте текст пустой строкой.',
    )
    list_items = models.TextField(
        blank=True,
        verbose_name='Пункты списка',
        help_text='Каждый пункт с новой строки.',
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Секция политики конфиденциальности'
        verbose_name_plural = 'Секции политики конфиденциальности'

    def __str__(self):
        return self.title

    @property
    def paragraphs(self):
        return [
            ' '.join(paragraph.split())
            for paragraph in self.content.split('\n\n')
            if paragraph.strip()
        ]

    @property
    def items(self):
        return [
            item.strip()
            for item in self.list_items.splitlines()
            if item.strip()
        ]
