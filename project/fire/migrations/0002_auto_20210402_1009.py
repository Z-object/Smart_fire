# Generated by Django 3.1.7 on 2021-04-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('man', '男'), ('woman', '女')], max_length=15, null=True),
        ),
    ]
