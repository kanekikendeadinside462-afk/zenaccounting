
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_calculatorsettings_contactrequest_faq_servicecompany_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAccountingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('consultation', 'Консультация'), ('calculator', 'Калькулятор')], max_length=50)),
                ('service', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('tax_system', models.CharField(blank=True, max_length=255)),
                ('price', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Заявка ИП',
                'verbose_name_plural': 'Заявки ИП',
                'ordering': ['-created_at'],
            },
        ),
    ]
