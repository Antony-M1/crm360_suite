# Generated by Django 4.2 on 2023-10-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_masters_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='masters',
            name='path',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]