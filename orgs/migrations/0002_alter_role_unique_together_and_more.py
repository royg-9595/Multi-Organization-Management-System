# Generated by Django 5.1.3 on 2024-11-25 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='role',
            constraint=models.UniqueConstraint(condition=models.Q(('name__iexact', False)), fields=('organization', 'name'), name='unique_role_per_organization'),
        ),
    ]