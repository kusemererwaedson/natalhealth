from django.urls import path
from .views import landing_page, custom_logout
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('submit_pregnancy_details/', views.submit_pregnancy_details, name='submit_pregnancy_details'),
    path('profile/', views.profile, name='profile'),
    path('logout/', custom_logout, name='logout'),
]

# Append static URL patterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)