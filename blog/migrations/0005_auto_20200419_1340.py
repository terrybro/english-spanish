# Generated by Django 3.0.5 on 2020-04-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200419_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='docfile',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
