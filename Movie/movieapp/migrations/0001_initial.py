# Generated by Django 5.1.1 on 2024-10-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]
