# Generated by Django 3.0 on 2019-12-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
