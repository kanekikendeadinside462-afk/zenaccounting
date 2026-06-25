
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_ipaccountingrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_highlighted', models.BooleanField(default=False, verbose_name='Красная карточка')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Услуга ИП',
                'verbose_name_plural': 'Услуги ИП',
                'ordering': ['order'],
            },
        ),
    ]
