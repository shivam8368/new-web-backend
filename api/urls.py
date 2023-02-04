from django.urls import path, include
from rest_framework import routers
from .views import UploadFileView, VideoViewSet

# from .views import home

router = routers.DefaultRouter()
router.register(r'', VideoViewSet)



urlpatterns = [
    # path('', home, name='api.home'),
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('', include(router.urls)),
    
    
]
