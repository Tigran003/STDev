from django.urls import path, include
from rest_framework.routers import  DefaultRouter
from .views import RoomViewSet, MovieViewSet, ScheduleViewSet, OccupiedSeatViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static



router = DefaultRouter()


router.register("rooms", RoomViewSet)
router.register("movie", MovieViewSet)
router.register("schedule", ScheduleViewSet)
router.register("seat", OccupiedSeatViewSet)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


