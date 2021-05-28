# Generated by Django 3.2.3 on 2021-05-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('massage', models.TextField()),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
    ]
