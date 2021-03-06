# Generated by Django 3.0.4 on 2020-03-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_unternehmensprofil'),
    ]

    operations = [
        migrations.AddField(
            model_name='unternehmensprofil',
            name='kategorie',
            field=models.CharField(choices=[('LEB', 'Lebensmittel'), ('BAE', 'Bäckerei'), ('FLE', 'Fleischerei'), ('GET', 'Getränke'), ('DRO', 'Drogerie'), ('ELE', 'Elektronik'), ('HWO', 'Haushalt & Wohnen'), ('WEB', 'Werkeln & Basteln'), ('SPO', 'Sport'), ('UNT', 'Unterhaltung'), ('MOD', 'Mode'), ('APO', 'Apotheke'), ('KIO', 'Zeitungen & Kiosk')], default='APO', max_length=3),
            preserve_default=False,
        ),
    ]
