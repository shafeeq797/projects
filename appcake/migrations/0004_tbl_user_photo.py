# Generated by Django 4.2.3 on 2023-07-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcake', '0003_tbl_cake'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_user',
            name='photo',
            field=models.CharField(default=1, max_length=600),
            preserve_default=False,
        ),
    ]