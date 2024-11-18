import os
import django

# Use the absolute path to the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Initialize Django
django.setup()
from models import PregnancyDetails
from django.db.models import Count

# Find duplicates based on nin_number
duplicates = PregnancyDetails.objects.values('nin_number').annotate(count=Count('nin_number')).filter(count__gt=1)

for dup in duplicates:
    print(dup)
