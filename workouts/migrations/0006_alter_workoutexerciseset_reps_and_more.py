# Generated by Django 4.1 on 2022-08-31 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workouts", "0005_workoutexerciseset_reps_workoutexerciseset_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workoutexerciseset",
            name="reps",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="workoutexerciseset",
            name="weight",
            field=models.FloatField(),
        ),
    ]
