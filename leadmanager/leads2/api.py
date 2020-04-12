from leads2.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSeralizer

# Lead Viewset

class LeadViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSeralizer
    
    def get_queryset(self):
        return self.request.user.leads2.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    