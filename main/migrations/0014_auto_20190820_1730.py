# Generated by Django 2.2.4 on 2019-08-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_company_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.TextField(blank=True, default='', max_length=250),
        ),
    ]