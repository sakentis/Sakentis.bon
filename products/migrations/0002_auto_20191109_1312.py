# Generated by Django 2.1.5 on 2019-11-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='body',
            field=models.TextField(),
        ),
    ]
