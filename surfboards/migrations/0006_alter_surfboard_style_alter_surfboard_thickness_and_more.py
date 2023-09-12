# Generated by Django 4.2.5 on 2023-09-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surfboards', '0005_alter_surfboard_style_alter_surfboard_thickness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surfboard',
            name='style',
            field=models.CharField(choices=[('fish', 'Fish'), ('twin', 'Twin'), ('round', 'Round'), ('asym', 'Asym'), ('swallow-tail', 'Swallow-tail'), ('pin tail', 'Pin tail'), ('squash', 'Squash'), ('mini-simmons', 'Mini-simmons'), ('other', 'Other')], max_length=100, verbose_name='Tail Style'),
        ),
        migrations.AlterField(
            model_name='surfboard',
            name='thickness',
            field=models.FloatField(max_length=3),
        ),
        migrations.AlterField(
            model_name='surfboard',
            name='volume',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Volume, L'),
        ),
    ]