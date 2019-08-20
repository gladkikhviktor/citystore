# Generated by Django 2.2.4 on 2019-08-20 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190820_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.District'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.TextField(default='', max_length=250),
        ),
    ]
