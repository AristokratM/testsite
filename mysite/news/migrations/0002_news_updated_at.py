# Generated by Django 3.1.4 on 2020-12-06 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]