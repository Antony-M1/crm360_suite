# Generated by Django 4.2 on 2023-09-20 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_userau_abstract_user_alter_userau_hsc_mark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salutation',
            options={'verbose_name': 'Salutation'},
        ),
        migrations.AlterModelOptions(
            name='userau',
            options={'verbose_name': 'User'},
        ),
        migrations.RemoveField(
            model_name='userau',
            name='abstract_user',
        ),
        migrations.RemoveField(
            model_name='userau',
            name='hsc_mark',
        ),
    ]