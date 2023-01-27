import asyncio
from aiogram import executor
from domains.telegram_bot.main import dp
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'This command runs telegram bot'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **kwargs):
        executor.start_polling(dp, skip_updates=True)

