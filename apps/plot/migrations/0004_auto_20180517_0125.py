# Generated by Django 2.0.4 on 2018-05-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plot', '0003_auto_20180516_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]