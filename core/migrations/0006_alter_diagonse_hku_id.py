# Generated by Django 4.0.4 on 2022-05-06 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_diagonse_hku_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagonse',
            name='hku_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hkumember'),
        ),
    ]