import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a local superuser from environment variables when missing."

    def handle(self, *args, **options):
        user_model = get_user_model()
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin")
        if user_model.objects.filter(username=username).exists():
            self.stdout.write(f"Superuser {username} already exists.")
            return
        user = user_model(username=username, email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()
        self.stdout.write(f"Created superuser {username}.")
