from django.db import migrations


def seed_about_data(apps, schema_editor):
    AboutSection = apps.get_model('about', 'AboutSection')
    AboutStatistic = apps.get_model('about', 'AboutStatistic')

    # Seed the main section text and main stat
    AboutSection.objects.create(
        title="О КОМПАНИИ",
        description=(
            "Мы проводим геологическое изучение недр Казахстана, обеспечивая "
            "решение геологических задач в различных отраслях недропользования. "
            "Компания располагает квалифицированными кадрами, экспертизой, опытом "
            "и финансовой устойчивостью для оперативного и безопасного выполнения проектов."
        ),
        main_stat_description="Более 40 млрд тенге — общий объём государственного финансирования",
        main_stat_value="40",
        main_stat_has_plus=True
    )

    # Seed the bottom 3 statistics
    AboutStatistic.objects.create(
        description="Более 500 специалистов и экспертов",
        value="500",
        label="СПЕЦИАЛИСТОВ",
        order=1
    )
    AboutStatistic.objects.create(
        description="Работаем во всех регионах страны",
        value="14",
        label="РЕГИОНОВ",
        order=2
    )
    AboutStatistic.objects.create(
        description="Более 200 проектов с момента основания",
        value="200",
        label="+ПРОЕКТОВ",
        order=3
    )


def remove_about_data(apps, schema_editor):
    AboutSection = apps.get_model('about', 'AboutSection')
    AboutStatistic = apps.get_model('about', 'AboutStatistic')

    AboutSection.objects.all().delete()
    AboutStatistic.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_about_data, remove_about_data),
    ]
