# Generated by Django 3.2.5 on 2021-10-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_podpischiki'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]