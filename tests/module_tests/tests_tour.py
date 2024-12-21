from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest
from django.test import TestCase
from src.models import Tour
from src.views.tour_views import tour


class TourAppTests(TestCase):
    """Тесты для приложения Tour"""


    def test_create_tour_and_get_tour(self):
        image = UploadedFile(
            file=open('tests/uploads/test_image.png', 'rb'),
            name='image.png',
            content_type='image/png'
        )
        tour_info = dict(
            img=image,
            title="Tour title",
            description="Tour description",
            price=2300
        )
        tour_obj: Tour = Tour.objects.create(
            **tour_info
        )

        self.assertEqual(tour_obj.id, 1)

        request = HttpRequest()
        tour_page = tour(request, tour_obj.id)

        html = tour_page.content.decode('utf-8')
        self.assertIn(f"<title>Путешествие в {tour_obj.title} | Туристический сайт ЭТНО</title>", html)
