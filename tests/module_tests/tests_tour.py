from django.test import TestCase

class TourAppTests(TestCase):
    """Тесты для приложения Tour"""

    def setUp(self) -> None:
        ...

    def test_bad_maths(self) -> None:
        """Отрицательный тест"""
        self.assertEqual(1 + 1, 3)
