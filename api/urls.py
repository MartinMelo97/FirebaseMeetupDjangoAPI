from django.contrib import admin
from django.urls import path
from oxxo.views import ChelaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'chelas', ChelaViewSet)

urlpatterns = router.urls


urlpatterns += [
    path('admin/', admin.site.urls),
]
