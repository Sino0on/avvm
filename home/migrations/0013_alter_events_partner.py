# Generated by Django 4.1.1 on 2022-10-03 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_partner_alter_events_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.partner'),
        ),
    ]
