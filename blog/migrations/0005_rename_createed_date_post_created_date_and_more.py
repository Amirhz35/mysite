# Generated by Django 4.2.7 on 2024-03-01 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_createed_date_post_counted_veiw_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Createed_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titel',
            new_name='title',
        ),
    ]
