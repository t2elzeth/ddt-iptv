from django.test import TestCase
from django.contrib.staticfiles.finders import find

from .. import models


class TestShows(TestCase):
    def setUp(self) -> None:
        self.test_photo = find('tests/shows/test-photo.jpg')
        self.test_video = find('tests/shows/test-video.mp4')
        self.actor = models.Actor.objects.create(
            full_name="My test actor",
            photo=self.test_photo
        )
        self.show = models.Show.objects.create(
            title="My test show",
            rating=5,
            type="film",
            preview=self.test_photo,
            video=self.test_video,
            description="This is pushka description damn it",
            genre=['action', 'comedy']
        )
        self.show.actors.set([1])

    def test_show_repr(self):
        self.assertEquals(self.show.__str__(), f"{self.show.type.upper()}: «{self.show.title}»")
        self.assertGreater(self.show.rating, 0)
        self.assertLess(self.show.rating, 6)
