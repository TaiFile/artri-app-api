from django.urls import path

from .controllers import RemedyDetailView, RemedyListCreateView

urlpatterns = [
    path('remedies/', RemedyListCreateView.as_view(), name='remedy-list-create'),
    path('remedies/<int:pk>/', RemedyDetailView.as_view(), name='remedy-detail'),
]
