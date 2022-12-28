# Generated by Django 4.1.3 on 2022-12-28 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='totalInCents',
            new_name='total_in_cents',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customers.customer'),
        ),
    ]