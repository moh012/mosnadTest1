# Generated by Django 5.0 on 2024-08-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='rating',
        ),
        migrations.AddField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
