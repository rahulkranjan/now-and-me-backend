# Generated by Django 4.2 on 2023-05-04 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.role'),
        ),
    ]
