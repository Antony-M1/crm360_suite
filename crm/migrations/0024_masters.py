# Generated by Django 4.2 on 2023-10-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_author_blog_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
