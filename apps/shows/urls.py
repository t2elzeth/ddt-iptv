from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('shows', views.ShowViewSet)

urlpatterns = router.urls
