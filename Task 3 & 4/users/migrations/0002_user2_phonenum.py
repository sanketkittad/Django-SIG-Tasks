# Generated by Django 3.2.7 on 2021-09-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user2',
            name='phonenum',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]