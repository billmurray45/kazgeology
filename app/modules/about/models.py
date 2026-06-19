from django.db import models


class AboutSection(models.Model):
    title = models.CharField(
        max_length=100,
        default="О КОМПАНИИ",
        verbose_name="Заголовок секции"
    )
    description = models.TextField(
        verbose_name="Текст описания (абзац)"
    )
    main_stat_description = models.CharField(
        max_length=255,
        verbose_name="Описание главного показателя"
    )
    main_stat_value = models.CharField(
        max_length=50,
        verbose_name="Значение главного показателя"
    )
    main_stat_has_plus = models.BooleanField(
        default=True,
        verbose_name="Показывать плюс (+)"
    )

    class Meta:
        verbose_name = "Секция 'О компании'"
        verbose_name_plural = "Секция 'О компании'"

    def __str__(self):
        return self.title


class AboutStatistic(models.Model):
    description = models.CharField(
        max_length=255,
        verbose_name="Описание показателя"
    )
    value = models.CharField(
        max_length=50,
        verbose_name="Значение"
    )
    label = models.CharField(
        max_length=100,
        verbose_name="Подпись показателя (например: СПЕЦИАЛИСТОВ)"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок отображения"
    )

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Дополнительный показатель"
        verbose_name_plural = "Дополнительные показатели"

    def __str__(self):
        return f"{self.value} / {self.label}"


class AboutHistoryEvent(models.Model):
    year = models.PositiveIntegerField(verbose_name="Год")
    date_label = models.CharField(max_length=100, verbose_name="Дата")
    title = models.CharField(max_length=255, verbose_name="Заголовок события")
    description = models.TextField(verbose_name="Описание события")
    document_reference = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Ссылка на документ",
    )
    is_featured = models.BooleanField(default=False, verbose_name="Выделенная карточка")
    is_active = models.BooleanField(default=True, verbose_name="Показывать на сайте")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Событие истории компании"
        verbose_name_plural = "История компании"

    def __str__(self):
        return f"{self.year} — {self.title}"
