# Generated by Django 4.1.3 on 2022-11-09 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stud',
            old_name='name',
            new_name='branch',
        ),
        migrations.RemoveField(
            model_name='stud',
            name='parents_name',
        ),
        migrations.AddField(
            model_name='stud',
            name='course',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stud',
            name='parent_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stud',
            name='roll_no',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stud',
            name='s_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='stud',
            table='Stud_data',
        ),
    ]
