from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home
from .models import Workout

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_POST_creates_workout_and_redirects(self):
        response = self.client.post("/")
        self.assertEqual(Workout.objects.count(), 1)
        workout = Workout.objects.get(id=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, workout.get_absolute_url())


class WorkoutTest(TestCase):
    def test_get_absolute_url(self):
        workout = Workout.objects.create()
        self.assertEqual(workout.get_absolute_url(), f"/workouts/{workout.id}/")
