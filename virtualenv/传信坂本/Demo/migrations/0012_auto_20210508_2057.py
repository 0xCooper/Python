# Generated by Django 3.2 on 2021-05-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0011_rename_exploit_name_exploit_save_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exploitinfo_save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('exploit_mod', models.CharField(max_length=50, null=True)),
                ('exploit_rhost', models.CharField(max_length=20, null=True)),
                ('exploit_payload_type', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='exploit_save',
        ),
    ]
