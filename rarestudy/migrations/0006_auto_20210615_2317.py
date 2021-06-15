# Generated by Django 3.2.3 on 2021-06-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rarestudy', '0005_alter_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon_tag',
            field=models.PositiveSmallIntegerField(choices=[(0, '🐻'), (1, '🐶'), (2, '🐱'), (3, '🐘'), (4, '🐴'), (5, '🦁'), (6, '🦛'), (7, '🐯'), (8, '🐼'), (9, '🐵'), (10, '🐧'), (11, '🐏'), (12, '🐨'), (13, '🐿'), (14, '🐰'), (15, '🐷')], default=0),
        ),
    ]