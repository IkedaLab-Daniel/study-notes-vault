# Generated by Django 4.2.23 on 2025-07-13 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='LittleLemonAPI.category'),
        ),
    ]
