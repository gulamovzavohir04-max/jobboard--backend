from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Job
from .serializers import JobSerializer
from .permissions import IsOwnerOrReadOnly


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by("-created_at")
    serializer_class = JobSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "company", "location"]
    ordering_fields = ["created_at", "salary"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
