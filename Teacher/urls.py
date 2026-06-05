from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet

router = DefaultRouter()

router.register(
    'Teacher',
    TeacherViewSet,
    basename='Teacher'
)

urlpatterns = router.urls