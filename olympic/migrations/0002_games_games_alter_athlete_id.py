# Generated by Django 4.0.4 on 2022-05-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='games',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]