# Generated by Django 5.0.6 on 2024-05-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.CharField()),
                ('price', models.IntegerField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.CharField(max_length=80)),
            ],
        ),
    ]
