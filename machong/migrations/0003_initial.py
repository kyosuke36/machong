# Generated by Django 5.1.5 on 2025-02-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('machong', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
