
from rest_framework import routers
from produce import views

app_name = 'produce'

router = routers.DefaultRouter()
router.register(r'services_order', views.ServicesOrderViewSet, basename='produce')
router.register(r'services', views.ServicesViewSet, basename='produce')
router.register(r'', views.ProduceViewSet, basename='produce')
router.register(r'order', views.OrderViewSet, basename='produce')
urlpatterns = router.urls
