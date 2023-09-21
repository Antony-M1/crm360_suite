# Generated by Django 4.2 on 2023-09-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_alter_territory_parent_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('name', models.CharField(db_column='name', default='All Groups', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Customer Group',
                'db_table': 'tabCustomer Group',
            },
        ),
    ]
