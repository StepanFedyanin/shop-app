
from rest_framework import routers
from produce import views

app_name = 'produce'

router = routers.DefaultRouter()

router.register(r'', views.ProduceViewSet, basename='produce')

urlpatterns = router.urls
