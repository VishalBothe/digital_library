from django.db import migrations
from accounts.models import CustomUser


class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        user = CustomUser(
            name="Admin",
            email="vishalb2399@gmail.com",
            is_staff=True,
            is_superuser=True,
            mobile="9989789898"
        )
        user.set_password('12345')
        user.save()


    dependencies = []
    operations = [
        migrations.RunPython(seed_data),
    ]