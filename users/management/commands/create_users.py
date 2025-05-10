from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Create 20 users with realistic names and @scsa.ge emails'

    def handle(self, *args, **kwargs):
        user_data = [
            {"name": "James Smith", "email": "james.smith@scsa.ge"},
            {"name": "Emily Johnson", "email": "emily.johnson@scsa.ge"},
            {"name": "Michael Williams", "email": "michael.williams@scsa.ge"},
            {"name": "Olivia Brown", "email": "olivia.brown@scsa.ge"},
            {"name": "David Jones", "email": "david.jones@scsa.ge"},
            {"name": "Sophia Garcia", "email": "sophia.garcia@scsa.ge"},
            {"name": "William Miller", "email": "william.miller@scsa.ge"},
            {"name": "Ava Davis", "email": "ava.davis@scsa.ge"},
            {"name": "John Rodriguez", "email": "john.rodriguez@scsa.ge"},
            {"name": "Isabella Martinez", "email": "isabella.martinez@scsa.ge"},
            {"name": "Joseph Hernandez", "email": "joseph.hernandez@scsa.ge"},
            {"name": "Mia Lopez", "email": "mia.lopez@scsa.ge"},
            {"name": "Thomas Gonzalez", "email": "thomas.gonzalez@scsa.ge"},
            {"name": "Charlotte Wilson", "email": "charlotte.wilson@scsa.ge"},
            {"name": "Daniel Anderson", "email": "daniel.anderson@scsa.ge"},
            {"name": "Amelia Thomas", "email": "amelia.thomas@scsa.ge"},
            {"name": "Matthew Taylor", "email": "matthew.taylor@scsa.ge"},
            {"name": "Harper Moore", "email": "harper.moore@scsa.ge"},
            {"name": "Anthony Jackson", "email": "anthony.jackson@scsa.ge"},
            {"name": "Evelyn Martin", "email": "evelyn.martin@scsa.ge"},
        ]

        shared_password = "Ragaca123"
        created_users = []

        for data in user_data:
            # Split full name into first and last name
            name_parts = data["name"].split(" ", 1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else "" # last_name = second part if it exists, else ""

            if CustomUser.objects.filter(email=data["email"]).exists():
                # self.stdout.write(...) is preferred over print() in Django management commands
                self.stdout.write(self.style.WARNING(f"{data['email']} already exists. Skipping."))
                # The continue statement:
                # Skip the rest of the loop body for the current item.
                # Move on to the next item in the loop.
                continue

            user = CustomUser.objects.create_user(
                email=data["email"],
                first_name=first_name,
                last_name=last_name,
                password=shared_password,
                is_active=True,
                is_staff=False,
            )

            created_users.append(user.email)
            self.stdout.write(self.style.SUCCESS(f"Created {user.email} - {first_name} {last_name}"))

        # Create superuser only once
        admin_email = "admin@gmail.com"
        if not CustomUser.objects.filter(email=admin_email).exists():
            super_user = CustomUser.objects.create_superuser(
                email=admin_email,
                password="admin"
            )
            self.stdout.write(self.style.SUCCESS(f"\n✅ Superuser: {super_user.email} created."))
        else:
            self.stdout.write(self.style.WARNING(f"\n⚠️ Superuser {admin_email} already exists. Skipping."))

        self.stdout.write(self.style.SUCCESS(f"\n✅ Total users created: {len(created_users)}"))
