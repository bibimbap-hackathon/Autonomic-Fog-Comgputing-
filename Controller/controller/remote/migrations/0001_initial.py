# Generated by Django 4.1.7 on 2023-02-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='모듈 이름')),
                ('giturl', models.CharField(max_length=50, verbose_name='모듈 깃헙')),
                ('install', models.TextField(verbose_name='설치 스크립트')),
                ('execute', models.TextField(verbose_name='실행 스크립트')),
                ('envs', models.JSONField(verbose_name='환경변수')),
            ],
        ),
        migrations.CreateModel(
            name='Remote',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='auto')),
                ('type', models.IntegerField()),
                ('ip', models.CharField(max_length=20, verbose_name='서버 아이피')),
                ('name', models.CharField(max_length=20, verbose_name='서버 이름')),
                ('rootpw', models.CharField(max_length=20, verbose_name='서버 비번')),
                ('cloud', models.CharField(max_length=20, verbose_name='상위 서버 아이피')),
            ],
        ),
    ]
