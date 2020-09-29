from django.contrib.auth.models import User


class RegistrationService:
    def register(self, email, first_name, last_name, password=None):
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        return user
