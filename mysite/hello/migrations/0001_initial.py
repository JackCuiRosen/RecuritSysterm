# Generated by Django 2.2.12 on 2024-07-26 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(150)])),
                ('province', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('hobby', models.CharField(max_length=25)),
                ('major', models.CharField(choices=[(1, '软件工程'), (2, '计算机科学'), (3, '网络安全'), (4, '电子信息'), (5, '数学'), (6, '统计学')], max_length=10)),
            ],
        ),
    ]
