# Generated by Django 3.2.4 on 2021-06-29 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_rename_battleid_battledata__id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='battledata',
            old_name='_id',
            new_name='battleID',
        ),
    ]
