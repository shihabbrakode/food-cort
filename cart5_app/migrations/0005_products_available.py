# Generated by Django 3.2.5 on 2021-08-04 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart5_app', '0004_alter_categ_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
    ]