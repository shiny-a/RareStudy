# Generated by Django 3.2.3 on 2021-06-18 15:02

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rarestudy', '0007_auto_20210617_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=mdeditor.fields.MDTextField(),
        ),
    ]