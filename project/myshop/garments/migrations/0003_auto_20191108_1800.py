# Generated by Django 2.2.6 on 2019-11-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garments', '0002_auto_20191108_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formalshirt',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
