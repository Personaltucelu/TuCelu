# Generated by Django 3.1.3 on 2020-11-07 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcelu', '0003_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celular',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcelu.marca'),
        ),
    ]
