# Generated by Django 3.2.2 on 2021-05-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmgr', '0003_alter_task_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
