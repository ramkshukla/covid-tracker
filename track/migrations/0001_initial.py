# Generated by Django 3.1.4 on 2020-12-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('cases', models.CharField(max_length=100)),
                ('deaths', models.CharField(max_length=100)),
                ('recovered', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'API DATA',
                'verbose_name_plural': 'APIS DATA',
            },
        ),
    ]
