# Generated by Django 3.0.2 on 2020-03-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FundooNotes', '0008_auto_20200306_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
