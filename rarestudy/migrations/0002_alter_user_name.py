# Generated by Django 3.2.3 on 2021-06-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rarestudy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='user', max_length=50),
        ),
    ]
