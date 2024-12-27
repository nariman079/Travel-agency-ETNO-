from dataclasses import asdict
from typing import Dict

from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from telebot import TeleBot

from src.base_dataclasses import ResponseMessage
from src.models.application_models import ApplicationTour


class ApplicationTourCreateSrv:
    """ Создание заявки и отправка сообщения """

    def __init__(self, body: Dict[str, str]):
        try:
            self.full_name = body["full_name"]
            self.phone_number = body["email"]
            self.tour_id = body['tour_title']
        except KeyError as error:
            raise ValidationError(asdict(
                ResponseMessage(
                    success=False,
                    data=None,
                    message=' '.join(error.args)
                )
            )
            )

    def _generate_message(self) -> None:
        """ Генерация текста сообщения """
        self.message_text = f"""Новая заявка!
        Тур: {settings.SITE_URL}/{settings.CONTENT_ADMIN_URL}/tour/{self.tour_id}
        Имя: {self.full_name}
        Номер телефона: {self.phone_number}
        """

    def _create_application_tour(self) -> None:
        """ Создание заявки """
        ApplicationTour.objects.create(
            full_name=self.full_name,
            phone_number=self.phone_number,
            tour_id=self.tour_id
        )

    def _send_message_on_telegram(self) -> None:
        """ Отправка сообщения на telegram """
        bot = TeleBot(settings.TELEGRAM_BOT_TOKEN)
        bot.send_message(
            chat_id=settings.TELEGRAM_CHAT_ID,
            text=self.message_text
        )

    def execute(self) -> Response:
        self._generate_message()
        self._create_application_tour()
        self._send_message_on_telegram()
        return Response(
            asdict(
                ResponseMessage(
                    message="Заявка успешно создана",
                    success=True,
                    data=None
                )
            ),
            status=201
        )
