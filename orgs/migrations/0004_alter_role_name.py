# Generated by Django 5.1.3 on 2024-11-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0003_remove_role_unique_role_per_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
