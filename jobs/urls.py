from django.urls import path
from .views import JobListCreateView, JobRetrieveUpdateDeleteView

urlpatterns = [
    path("jobs/", JobListCreateView.as_view()),
    path("jobs/<int:pk>/", JobRetrieveUpdateDeleteView.as_view()),
]
