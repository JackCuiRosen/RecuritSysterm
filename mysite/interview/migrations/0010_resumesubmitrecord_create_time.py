# Generated by Django 4.2.14 on 2024-08-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0009_alter_qqgroup_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumesubmitrecord',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
