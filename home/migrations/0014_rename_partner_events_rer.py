# Generated by Django 4.1.1 on 2022-10-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_events_partner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='partner',
            new_name='rer',
        ),
    ]
