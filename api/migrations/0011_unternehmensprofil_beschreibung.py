# Generated by Django 3.0.4 on 2020-03-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200321_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='unternehmensprofil',
            name='beschreibung',
            field=models.TextField(default='Ein großartiges Beispiel Unternehmen'),
            preserve_default=False,
        ),
    ]
