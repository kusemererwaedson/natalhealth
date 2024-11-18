from django.db import models


class BabyWeek(models.Model):
    week_number = models.PositiveIntegerField(unique=True)
    image = models.ImageField(upload_to='baby_images/')
    average_weight = models.DecimalField(max_digits=8, decimal_places=4, help_text="Weight in kilograms")
    average_size = models.DecimalField(max_digits=5, decimal_places=2, help_text="Size in centimeters")

    def __str__(self):
        return f"Week {self.week_number}"

class PregnancyDetails(models.Model):
    nin = models.CharField(max_length=20, unique=True) 
    name = models.CharField(max_length=20)
    baby_sex = models.CharField(max_length=20)
    due_date_choice = models.CharField(max_length=50)
    due_date = models.DateField(null=True, blank=True)
    first_child = models.CharField(max_length=3)
    age_group = models.CharField(max_length=20)

    def __str__(self):
        return f"Pregnancy details for {self.baby_sex}"

class InsightCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Insight(models.Model):
    category = models.ForeignKey(InsightCategory, on_delete=models.CASCADE, related_name='insights')
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='insights_images/', null=True, blank=True)

    def __str__(self):
        return self.title