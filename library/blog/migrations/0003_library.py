# Generated by Django 3.0.5 on 2020-04-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('personal_library', models.TextField()),
            ],
        ),
    ]