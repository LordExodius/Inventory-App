# Generated by Django 4.0.1 on 2022-01-19 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0002_rename_itemnum_item_numitems_remove_item_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='itemName',
            field=models.TextField(verbose_name='item name'),
        ),
    ]
