# Generated by Django 3.2.18 on 2023-04-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('management', 'management'), ('support', 'support'), ('sale', 'sale')], max_length=50, null=True),
        ),
    ]
