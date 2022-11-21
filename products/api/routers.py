from rest_framework.routers import DefaultRouter
from products.api.views.product_views import ProductViewSet

router = DefaultRouter()


router.register(r'products', ProductViewSet)


urlpatterns = router.urls


