from rest_framework.routers import DefaultRouter
from products.api.views.product_views import ProductViewSet
from products.api.views.general_views import CategoryProductListAPIView, IndicadorListAPIView, MeasureUnitListAPIView

router = DefaultRouter()


router.register(r'products', ProductViewSet, basename='products')
router.register(r'measure_unit', MeasureUnitListAPIView, basename='measure_unit')
router.register(r'category_product', CategoryProductListAPIView, basename='category_product')
router.register(r'indicador', IndicadorListAPIView, basename='indicador')


urlpatterns = router.urls


