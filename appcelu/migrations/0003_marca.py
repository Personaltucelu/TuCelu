# Generated by Django 3.1.3 on 2020-11-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcelu', '0002_auto_20201106_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
    ]