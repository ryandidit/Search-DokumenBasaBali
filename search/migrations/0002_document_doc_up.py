# Generated by Django 3.1.3 on 2020-11-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='doc_up',
            field=models.FileField(null=True, upload_to='doc'),
        ),
    ]