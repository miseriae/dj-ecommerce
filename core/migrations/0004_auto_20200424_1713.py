# Generated by Django 3.0.4 on 2020-04-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='one_click_purchasing',
            field=models.BooleanField(default=False),
        ),
    ]
