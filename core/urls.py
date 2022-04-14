from django.urls import path, include
from .api_views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'venues', VenueViewSet, 'venue')
router.register(r'records', RecordViewSet, 'record')
urlpatterns=[
    path('api/venues_visited/<int:hku_id>', get_venues_visited),
    path('api/close_contacts/<int:hku_id>', get_close_contacts),
    # path('api/venues', all_venues),
    # path('api/records', all_records),
    path('api/', include(router.urls)),
]