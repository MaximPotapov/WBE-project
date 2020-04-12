from rest_framework import routers
from .api import LeadViewSet

from django.urls import path
from .views import current_user, UserList

router = routers.DefaultRouter()
router.register('api/leads2', LeadViewSet, 'leads2')

urlpatterns = router.urls 

