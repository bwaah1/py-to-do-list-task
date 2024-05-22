# Generated by Django 4.1 on 2024-05-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(choices=[('DONE', 'Done'), ('NOT DONE', 'Not done')], max_length=8)),
                ('deadline', models.DateTimeField()),
                ('tags', models.ManyToManyField(related_name='tags', to='tasks.tag')),
            ],
        ),
    ]
