# Generated by Django 2.2.6 on 2019-10-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Template Title')),
                ('description', models.TextField()),
                ('image_url', models.CharField(max_length=300, verbose_name='Template Image Url')),
                ('color', models.CharField(max_length=10, verbose_name='Template Color')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
