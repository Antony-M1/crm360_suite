# Generated by Django 4.2 on 2023-09-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_alter_gender_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(db_column='source_name', help_text='To mention the which platform we get this source', max_length=255, unique=True, verbose_name='Source Name')),
                ('details', models.TextField(blank=True, db_column='details', help_text='Mention more details about the source', null=True, verbose_name='Source Details')),
            ],
            options={
                'verbose_name': 'Lead Source',
                'db_table': 'tabLead Source',
            },
        ),
    ]
