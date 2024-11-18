import os
import django

# Set the environment variable for the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'natal_health.settings')

# Initialize Django
django.setup()

from main.models import PregnancyDetails

# Test if we can fetch all records from the PregnancyDetails model
pregnancy_details = PregnancyDetails.objects.all()
print(pregnancy_details)  # This should print a queryset or an empty list

# Optionally, print out the first record to check if fetching works
if pregnancy_details:
    print(pregnancy_details[0])
else:
    print("No PregnancyDetails records found.")
