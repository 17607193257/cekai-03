# Generated by Django 3.0 on 2019-12-18 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects_age1'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='age2',
            field=models.IntegerField(null=True),
        ),
    ]
