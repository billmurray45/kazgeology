from io import BytesIO
import os
import uuid

from django.db import models
from django.templatetags.static import static
from PIL import Image, ImageOps


def board_member_photo_upload_to(instance, filename):
    extension = os.path.splitext(filename)[1].lower() or '.jpg'
    return f'board/members/{uuid.uuid4().hex}{extension}'


def optimize_image_file(path):
    if not path or not os.path.exists(path):
        return

    with Image.open(path) as image:
        image_format = image.format
        if image_format not in ('JPEG', 'PNG', 'WEBP'):
            return

        output = BytesIO()

        if image_format == 'JPEG':
            save_kwargs = {
                'format': 'JPEG',
                'quality': 'keep',
                'subsampling': 'keep',
                'qtables': 'keep',
                'optimize': True,
                'progressive': True,
            }
            if image.info.get('exif'):
                save_kwargs['exif'] = image.info['exif']

            try:
                image.save(output, **save_kwargs)
            except ValueError:
                if image.mode not in ('RGB', 'L'):
                    image = image.convert('RGB')
                image.save(output, format='JPEG', quality=100, subsampling=0, optimize=True)
        elif image_format == 'PNG':
            image = ImageOps.exif_transpose(image)
            image.save(output, format='PNG', optimize=True, compress_level=9)
        else:
            image = ImageOps.exif_transpose(image)
            image.save(output, format='WEBP', lossless=True, quality=100, method=6)

    optimized = output.getvalue()
    if optimized and len(optimized) < os.path.getsize(path):
        with open(path, 'wb') as image_file:
            image_file.write(optimized)


class BoardMember(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    role = models.CharField(max_length=255, verbose_name='Роль')
    photo = models.ImageField(
        upload_to=board_member_photo_upload_to,
        blank=True,
        verbose_name='Фото',
    )
    is_chair = models.BooleanField(default=False, verbose_name='Председатель')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Член Совета директоров'
        verbose_name_plural = 'Члены Совета директоров'

    def __str__(self):
        return self.full_name

    @property
    def photo_url(self):
        if not self.photo:
            return ''

        if self.photo.name.startswith('images/'):
            return static(self.photo.name)

        return self.photo.url

    def save(self, *args, **kwargs):
        photo_changed = self._photo_has_changed()
        super().save(*args, **kwargs)

        if photo_changed and self.photo:
            optimize_image_file(self.photo.path)

    def _photo_has_changed(self):
        if not self.pk:
            return bool(self.photo)

        try:
            old_photo = type(self).objects.only('photo').get(pk=self.pk).photo
        except type(self).DoesNotExist:
            return bool(self.photo)

        return old_photo.name != self.photo.name


class BoardSecretary(models.Model):
    label = models.CharField(max_length=255, verbose_name='Должность')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    class Meta:
        verbose_name = 'Корпоративный секретарь'
        verbose_name_plural = 'Корпоративный секретарь'

    def __str__(self):
        return self.full_name


class BoardCommittee(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название комитета')
    count_label = models.CharField(max_length=50, verbose_name='Подпись количества')
    icon_class = models.CharField(
        max_length=100,
        default='fa-solid fa-users',
        verbose_name='CSS-класс иконки',
        help_text='Например: fa-solid fa-chart-line',
    )
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Комитет Совета директоров'
        verbose_name_plural = 'Комитеты Совета директоров'

    def __str__(self):
        return self.title


class BoardCommitteeMember(models.Model):
    committee = models.ForeignKey(
        BoardCommittee,
        on_delete=models.CASCADE,
        related_name='members',
        verbose_name='Комитет',
    )
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    note = models.CharField(max_length=255, blank=True, verbose_name='Примечание')
    role_label = models.CharField(max_length=50, blank=True, verbose_name='Метка роли')
    is_chair = models.BooleanField(default=False, verbose_name='Председатель')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Участник комитета'
        verbose_name_plural = 'Участники комитетов'

    def __str__(self):
        return f'{self.full_name} — {self.committee}'
