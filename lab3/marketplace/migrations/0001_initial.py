# Generated by Django 4.0.4 on 2022-05-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(default='', max_length=500)),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
