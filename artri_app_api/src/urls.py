from django.urls import path, include

urlpatterns = [
    path('', include('src.domains.accounts.urls')),
    path('', include('src.domains.remedies.urls')),
    path('', include('src.domains.exercises.urls')),
    path('', include('src.domains.reports.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
