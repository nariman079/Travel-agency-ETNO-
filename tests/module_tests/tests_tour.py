from datetime import datetime, timedelta

from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest
from django.test import TestCase
from django.db.models import F, Value, Func, CharField
from django.db.models.functions import Cast

from django.core.files.uploadedfile import SimpleUploadedFile

from src.models import Tour, Report, ApplicationTour
from src.services.tour_services import create_report
from src.views.tour_views import tour


class TourAppTests(TestCase):
    """Тесты для приложения Tour"""

    def test_create_tour_and_get_tour(self):
        image = SimpleUploadedFile(
            content=open('tests/uploads/test_image.png', 'rb').read(),
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


class ReportTest(TestCase):
    def setUp(self):
        self.tour = Tour.objects.create(
            title="Test title",
            description="Test description",
            img=SimpleUploadedFile(
                content=open('tests/uploads/test_image.png', 'rb').read(),
                name="image_.png",
                content_type='image/png'
            ),
            price=3000
        )
        [
            ApplicationTour.objects.create(
                full_name=f"Test user {i}",
                phone_number=f"8329-{i}",
                tour_id=self.tour.pk
            ) for i in range(100)
        ]
    
    def test_report_create_fucn(self):
        report_obj = Report.objects.create(
            report_type='day',
        )
        dates = {
            'day': 24,
            'week': 24*7,
            'month': 24*30
        }
    
        search_date = datetime.now() - timedelta(hours=dates[report_obj.report_type])
        application_tours = ApplicationTour.objects.filter(date_created__gte=search_date)
        qur = application_tours.annotate(
            create_at=Cast('date_created', output_field=CharField())).values('full_name', 'phone_number', 'tour__title', 'status', 'create_at')
        report_data = create_report(report_obj, qur)
        report_obj.refresh_from_db()
        
        self.assertEqual(report_obj.file.name, f"reports/report_{report_obj.uid}.xlsx")
        self.assertEqual(report_data, qur)