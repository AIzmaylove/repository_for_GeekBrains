# Generated by Django 3.2 on 2022-08-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link_to_repo',
            field=models.URLField(max_length=120, null=True),
        ),
    ]
