# Generated by Django 3.1.5 on 2021-01-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'product_Table',
            },
        ),
    ]
