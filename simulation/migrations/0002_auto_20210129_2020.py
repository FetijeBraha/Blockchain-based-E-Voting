# Generated by Django 2.2.13 on 2021-01-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='block',
            name='name',
        ),
        migrations.RemoveField(
            model_name='block',
            name='komuna',
        ),
        migrations.AlterField(
            model_name='vote',
            name='LastName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vote',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vote',
            name='komuna',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='votebackup',
            name='LastName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='votebackup',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='votebackup',
            name='komuna',
            field=models.CharField(max_length=200),
        ),
    ]
