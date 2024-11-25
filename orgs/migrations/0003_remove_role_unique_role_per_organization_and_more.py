# Generated by Django 5.1.3 on 2024-11-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0002_alter_role_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='role',
            name='unique_role_per_organization',
        ),
        migrations.AddConstraint(
            model_name='role',
            constraint=models.UniqueConstraint(fields=('organization', 'name'), name='unique_role_per_organization'),
        ),
    ]
