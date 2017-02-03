from django.conf.urls import url, include
from rest_framework import routers
from musical_api import views

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistsViewSet)
router.register(r'genres', views.GenresViewSet)
router.register(r'albums', views.AlbumsViewSet)
router.register(r'songs', views.SongsViewSet)
router.register(r'customers', views.CustomersViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]