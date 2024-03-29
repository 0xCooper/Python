# Generated by Django 3.2 on 2021-05-08 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0006_console_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act_info',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='console_status',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='console_status',
            name='prompt',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='msf_status',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='online',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
