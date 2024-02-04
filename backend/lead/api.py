from rest_framework.serializers import Serializer
from lead.models import *
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead viewset
class leadViewSet (viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.lead.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)