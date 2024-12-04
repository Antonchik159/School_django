# Generated by Django 5.1.3 on 2024-12-04 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0008_alter_teacher_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="school.subject",
                verbose_name="Предмет який викладає",
            ),
        ),
    ]
