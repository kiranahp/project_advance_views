# Generated by Django 2.1.5 on 2019-02-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mentee_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_mentee', models.TextField(max_length=50)),
                ('quotes_mentee', models.TextField()),
                ('foto_mentee', models.ImageField(upload_to='menteemedia')),
            ],
        ),
    ]
