# Generated by Django 2.1.5 on 2020-04-23 11:16

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bells', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='detail',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
