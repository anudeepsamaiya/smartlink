# Generated by Django 2.2 on 2019-06-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
