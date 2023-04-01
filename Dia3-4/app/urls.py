from rest_framework import routers
from app.views import ToDoViewSet

router = routers.DefaultRouter()

router.register(r'api', ToDoViewSet)

urlpatterns = router.urls