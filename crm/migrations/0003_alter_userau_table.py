# Generated by Django 4.2 on 2023-09-20 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_userau_options_alter_user_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userau',
            table='tabUser',
        ),
    ]