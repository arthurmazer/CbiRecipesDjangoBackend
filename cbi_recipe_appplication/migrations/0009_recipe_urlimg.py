# Generated by Django 4.2.5 on 2023-10-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbi_recipe_appplication', '0008_alter_recipe_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='urlImg',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
