# Generated by Django 4.1 on 2022-08-28 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("workouts", "0002_workoutexercise"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workoutexercise",
            name="workout",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exercises",
                to="workouts.workout",
            ),
        ),
    ]