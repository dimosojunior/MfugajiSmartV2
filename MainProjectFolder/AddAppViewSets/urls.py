
from django.urls import path
from . import views

# # MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('AllMikoa', views.AllMikoaViewSet)
router.register('LevelZaWafugaji', views.LevelZaWafugajiViewSet)
router.register('AinaZaKukuViewSet', views.AinaZaKukuViewSet)
router.register('UserRoleViewSet', views.UserRoleViewSet)
router.register('UserStatusViewSet', views.UserStatusViewSet)
router.register('MudaWaKumbushoUsafishajiBandaViewSet', views.MudaWaKumbushoUsafishajiBandaViewSet)
router.register('AinaZaChanjoViewSet', views.AinaZaChanjoViewSet)
router.register('UmriWaKukuViewSet', views.UmriWaKukuViewSet)
router.register('AinaZaNdegeViewSet', views.AinaZaNdegeViewSet)





urlpatterns = router.urls