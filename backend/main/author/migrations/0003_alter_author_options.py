# Generated by Django 4.2.4 on 2023-08-11 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('pk',)},
        ),
    ]
