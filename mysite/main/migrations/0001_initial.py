# Generated by Django 3.1.7 on 2021-08-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('is_main', models.BooleanField()),
            ],
        ),
    ]
