# Generated by Django 4.1 on 2022-10-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workouts", "0013_workout_routine"),
    ]

    operations = [
        migrations.AddField(
            model_name="workoutexercise",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]