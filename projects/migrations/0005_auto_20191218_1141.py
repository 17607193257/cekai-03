# Generated by Django 3.0 on 2019-12-18 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20191218_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='pdesc',
            new_name='desc',
        ),
    ]
