# Generated by Django 3.0.6 on 2020-06-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize_main', '0008_auto_20200623_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='university',
            field=models.CharField(default='', max_length=1000, verbose_name='university'),
        ),
    ]
