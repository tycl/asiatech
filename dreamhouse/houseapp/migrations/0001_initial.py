# Generated by Django 2.1.7 on 2019-03-05 17:13

from django.db import migrations, models
import houseapp.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(blank=True, default='', max_length=250)),
                ('name', models.CharField(blank=True, default='', max_length=250)),
                ('address', models.CharField(blank=True, default='', max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('upload', models.FileField(upload_to=houseapp.models.user_directory_path)),
                ('macnum', models.UUIDField(default=uuid.uuid1, editable=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
