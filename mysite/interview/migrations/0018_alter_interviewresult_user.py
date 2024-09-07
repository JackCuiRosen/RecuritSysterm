# Generated by Django 4.2.14 on 2024-08-26 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0017_alter_interviewresult_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewresult',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
