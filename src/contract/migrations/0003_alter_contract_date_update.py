# Generated by Django 3.2.18 on 2023-04-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_alter_contract_sales_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
