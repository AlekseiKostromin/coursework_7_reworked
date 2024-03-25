from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='cs777@yandex.ru',
            first_name='Aleksei',
            last_name='Ko',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password('12345')
        user.save()
