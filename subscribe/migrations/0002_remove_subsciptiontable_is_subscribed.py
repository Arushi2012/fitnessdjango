# Generated by Django 2.0.7 on 2018-07-22 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsciptiontable',
            name='is_subscribed',
        ),
    ]