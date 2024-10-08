# Generated by Django 4.2.3 on 2024-09-29 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_remove_manager_unique_id_alter_manager_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateField()),
                ('designation', models.CharField(max_length=100)),
                ('manager_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='rest_api.manager')),
            ],
        ),
    ]
