from rest_framework import routers, urlpatterns
from .api import leadViewSet


router = routers.DefaultRouter()
router.register('api/lead', leadViewSet, 'lead')

urlpatterns = router.urls