# Generated by Django 4.1.6 on 2023-02-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]