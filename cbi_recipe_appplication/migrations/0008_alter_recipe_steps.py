# Generated by Django 4.2.5 on 2023-10-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbi_recipe_appplication', '0007_alter_recipe_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.ManyToManyField(to='cbi_recipe_appplication.instruction'),
        ),
    ]
