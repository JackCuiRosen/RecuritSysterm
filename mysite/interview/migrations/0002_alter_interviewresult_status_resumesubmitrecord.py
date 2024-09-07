# Generated by Django 4.2.14 on 2024-08-23 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_candidate_advantage_alter_candidate_education_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewresult',
            name='status',
            field=models.CharField(choices=[(0, '不建议录取'), (1, '建议录取'), (2, '建议进行二面'), (3, '待定')], default=3, max_length=10),
        ),
        migrations.CreateModel(
            name='resumeSubmitRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50, verbose_name='部门')),
                ('qqgroup_id', models.CharField(max_length=50, verbose_name='面试通知群组')),
                ('final_grade', models.FloatField(verbose_name='最终成绩')),
                ('interviweResult1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='FirstInterview', to='interview.interviewresult')),
                ('interviweResult2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='SecondInterview', to='interview.interviewresult')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
