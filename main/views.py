from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PregnancyDetails, BabyWeek, InsightCategory
from django.contrib.auth import logout
from django.db import IntegrityError

# # View for landing page
# def landing_page(request):
#     weeks = BabyWeek.objects.all().order_by('week_number')
#     categories = InsightCategory.objects.prefetch_related('insights')
#     return render(request, 'main/index.html', {'weeks': weeks, 'Categories': categories})

def landing_page(request):
    weeks = BabyWeek.objects.all().order_by('week_number')
    categories = InsightCategory.objects.prefetch_related('insights')

    # Fetch user's pregnancy details using session data
    pregnancy_details = None
    user_nin = request.session.get('user_nin')
    if user_nin:
        pregnancy_details = PregnancyDetails.objects.filter(nin=user_nin).first()

    return render(request, 'main/index.html', {
        'weeks': weeks,
        'Categories': categories,
        'pregnancy_details': pregnancy_details,  # Pass the user's details
    })



def submit_pregnancy_details(request):
    if request.method == 'POST':
        nin = request.POST.get('nin')
        name = request.POST.get('name')
        baby_sex = request.POST.get('baby_sex')
        due_date_choice = request.POST.get('due_date_choice')
        due_date = request.POST.get('due_date')
        first_child = request.POST.get('first_child') == 'true'
        age_group = request.POST.get('age_group')

        # Check if the user is logged in via session
        user_nin = request.session.get('user_nin')

        # Update the existing record or create a new one
        if user_nin:
            pregnancy_details = PregnancyDetails.objects.filter(nin=user_nin).first()
            if pregnancy_details:
                pregnancy_details.name = name
                pregnancy_details.baby_sex = baby_sex
                pregnancy_details.due_date_choice = due_date_choice
                pregnancy_details.due_date = due_date
                pregnancy_details.first_child = first_child
                pregnancy_details.age_group = age_group
                pregnancy_details.save()
                messages.success(request, "Your details have been updated.")
                return redirect('profile')
        
        try:
            # Create a new record
            new_record = PregnancyDetails.objects.create(
                nin=nin,
                name=name,
                baby_sex=baby_sex,
                due_date_choice=due_date_choice,
                due_date=due_date,
                first_child=first_child,
                age_group=age_group
            )
            # Update session with new NIN
            request.session['user_nin'] = new_record.nin
            messages.success(request, "Your details have been saved.")
            return redirect('profile')
        except IntegrityError:
            # Handle the unique constraint error
            messages.error(request, "A record with this NIN already exists.")
            return redirect('profile')


def profile(request):
    # Check if the user has a valid session (NIN)
    nin = request.session.get('user_nin')

    # Fetch the categories for insights modal
    categories = InsightCategory.objects.prefetch_related('insights')

    pregnancy_details = None  # Default to None

    if nin:
        try:
            # Attempt to fetch pregnancy details using the NIN from the session
            pregnancy_details = PregnancyDetails.objects.get(nin=nin)
        except PregnancyDetails.DoesNotExist:
            messages.error(request, "Pregnancy details not found.")
            return redirect('landing_page')  # Redirect to a safe page like the landing page

    if request.method == 'POST':
        # Get the NIN from the POST data
        nin = request.POST.get('nin')

        if nin:
            try:
                # Attempt to get the PregnancyDetails object using the provided NIN
                pregnancy_details = PregnancyDetails.objects.get(nin=nin)

                # Store the NIN in the session so the user is logged in
                request.session['user_nin'] = pregnancy_details.nin  # Storing NIN in session
                
                messages.success(request, f"Welcome {pregnancy_details.name}! You are now logged in.")
                return redirect('profile')  # Redirect to the profile page after login

            except PregnancyDetails.DoesNotExist:
                # If the NIN is not found in the database, show an error message
                messages.error(request, "Invalid NIN. Please try again.")
                return render(request, 'main/profile.html')  # Re-render the NIN form
                
        else:
            messages.error(request, "NIN is required.")
            return render(request, 'main/profile.html')  # Re-render the NIN form
    
    # Render the profile page when visiting via GET, passing categories for the modal as well
    return render(request, 'main/profile.html', {
        'pregnancy_details': pregnancy_details,
        'Categories': categories,  # Pass categories for the modal
        'form_submitted': False
    })



def custom_logout(request):
    logout(request)  # Log the user out
    request.session.flush()  # Clear any session data
    messages.success(request, f"You are now logged out.")
    return redirect('landing_page')

