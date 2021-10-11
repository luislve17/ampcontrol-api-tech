import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--username', help="Admin's username", type=str)
        parser.add_argument('--email', help="Admin's email", type=str)
        parser.add_argument('--password', help="Admin's password", type=str)
        parser.add_argument('--no-input', action='store_true', help="Non-argumental execution using ENV")

    def handle(self, *args, **options):
        print("Handling superuser creation")
        User = get_user_model()
        if options['no_input']:
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME'),
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD'),
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL'),
        else:
            username = options['username']
            password = options['password']
            email = options['email']

        username = str(username[0])
        password = str(password[0])
        email = str(email[0])

        if not User.objects.filter(username=username).exists():
            print(f"> Superuser not found. Creating new one ({username}:{email})")
            User.objects.create_superuser(username=username,
                                        email=email,
                                        password=password)
        else:
            print(f"> Superuser already present in users list. Continuing...")