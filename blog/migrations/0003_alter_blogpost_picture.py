# Generated by Django 4.2 on 2023-04-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
