# Generated by Django 2.1.5 on 2019-02-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mentor_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_mentor', models.TextField(max_length=50)),
                ('proffesion_mentor', models.TextField(max_length=50)),
                ('quotes_mentor', models.TextField()),
                ('foto_mentor', models.ImageField(upload_to='mentormedia')),
            ],
        ),
    ]
