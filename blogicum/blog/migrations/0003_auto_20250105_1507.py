# Generated by Django 3.2.16 on 2025-01-05 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20250105_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_at',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='test',
            new_name='text',
        ),
    ]
