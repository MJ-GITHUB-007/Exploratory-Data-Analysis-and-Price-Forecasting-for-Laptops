# Generated by Django 4.2.1 on 2023-06-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input_data',
            name='CPU_Frequency',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='input_data',
            name='Memory_SSD',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='input_data',
            name='RAM',
            field=models.SmallIntegerField(),
        ),
    ]
