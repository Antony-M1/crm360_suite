# Generated by Django 4.2 on 2023-09-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_salutation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userau',
            name='abstract_user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userau',
            name='hsc_mark',
            field=models.IntegerField(blank=True, null=True, verbose_name='HSC Mark Verbose Name'),
        ),
    ]