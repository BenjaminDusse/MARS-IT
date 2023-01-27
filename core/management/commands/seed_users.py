import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django_seed import Seed
User = get_user_model()

NAME = 'users'


class Command(BaseCommand):
    help = 'This command creates {NAME}'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "tg_user_id": lambda x: random.randrange(100000000, 999999999),
                "chat_id": lambda x: random.randrange(100000000, 999999999),
                "is_staff": False,
                "is_superuser": False
            },
        )

        seeder.execute()
        # for i in range(number+1):
        #     User.objects.create(username=fake.name(), is_active=False)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
