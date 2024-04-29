from typing import Dict

from django.conf import settings
from rest_framework.exceptions import ValidationError
from telebot import TeleBot

from src.base_dataclasses import ResponseMessage


class SendMessageAboutApplication:
    """ Отправка сообщения при создании заявки """

    def __init__(self, body: Dict[str, str]):
        try:
            self.full_name = body["full_name"]
            self.phone_number = body["email"]
            self.tour_title = body['tour_title']
        except KeyError as error:
            raise ValidationError(
                ResponseMessage(
                    success=False,
                    data=None,
                    message=' '.join(error.args)
                )
            )

    def _generate_message(self) -> None:
        """ Генерация текста сообщения """
        self.message_text = f"""Новая заявка!
        Тур: {self.tour_title}
        Имя: {self.full_name}
        Номер телефона: {self.phone_number}
        """

    def _send_message_on_telegram(self) -> None:
        """ Отправка сообщения на telegram """
        bot = TeleBot(settings.TELEGRAM_BOT_TOKEN)
        bot.send_message(
            chat_id=settings.TELEGRAM_CHAT_ID,
            text=self.message_text
        )

    def execute(self) -> None:
        self._generate_message()
        self._send_message_on_telegram()