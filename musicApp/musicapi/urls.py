from django.urls import include, path 
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('songs', views.SongViewSet)
router.register('playlist', views.PlaylistViewSet)

urlpatterns = router.urls