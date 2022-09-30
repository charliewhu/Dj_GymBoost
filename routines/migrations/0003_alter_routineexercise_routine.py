# Generated by Django 4.1 on 2022-09-30 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("routines", "0002_routineexercise"),
    ]

    operations = [
        migrations.AlterField(
            model_name="routineexercise",
            name="routine",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exercises",
                to="routines.routine",
            ),
        ),
    ]
