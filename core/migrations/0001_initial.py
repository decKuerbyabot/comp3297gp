# Generated by Django 4.0.4 on 2022-05-06 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HKUMember',
            fields=[
                ('hku_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_code', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('LT', 'Lecture Theatre'), ('CR', 'Classroom'), ('TR', 'Tutorial Room')], max_length=2)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('event', models.CharField(choices=[('Entry', 'Entry - Event'), ('Exit', 'Exit - Event')], max_length=5)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hkumember')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venue')),
            ],
        ),
    ]
