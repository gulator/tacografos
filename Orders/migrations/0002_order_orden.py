# Generated by Django 4.1.1 on 2024-12-11 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orden',
            field=models.CharField(default='null', max_length=19),
            preserve_default=False,
        ),
    ]
