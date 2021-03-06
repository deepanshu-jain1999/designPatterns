# Generated by Django 3.0.3 on 2020-03-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='support@example.com', max_length=254)),
                ('work_email', models.EmailField(blank=True, max_length=254)),
                ('name', models.CharField(default='only_user', max_length=255)),
                ('city', models.CharField(default='jewar', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
