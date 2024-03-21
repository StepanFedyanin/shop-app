from rest_framework import routers
from user import views

router = routers.DefaultRouter()

router.register(r'', views.MyUserViewSet, basename='users')

app_name = 'account'
urlpatterns = router.urls



