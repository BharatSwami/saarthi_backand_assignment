# Generated by Django 3.2.9 on 2021-11-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20211124_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
