# Generated by Django 4.0.3 on 2022-03-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('author', models.CharField(max_length=200)),
                ('isnb', models.CharField(max_length=20)),
            ],
        ),
    ]