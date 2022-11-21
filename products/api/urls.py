from django.urls import path

from products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicadorListAPIView
from products.api.views.product_views import ProductListCreateApiView, ProductRetrieveUpdateDestroyApiView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicator/', IndicadorListAPIView.as_view(), name='indicator'),
    path('category_products/', CategoryProductListAPIView.as_view(), name='category_products'),
    path('products/', ProductListCreateApiView.as_view(), name='products'),
    path('products/<int:pk>', ProductRetrieveUpdateDestroyApiView.as_view(), name='products_RUD'),
    # path('products/list', ProductListApiView.as_view(), name='products_list'),
    # path('products/create', ProductCreateApiView.as_view(), name='product_create'),
    # path('products/retrieve/<int:pk>', ProductRetrieveApiView.as_view(), name='product_retrieve'),
    # path('products/destroy/<int:pk>', ProductDestroyApiView.as_view(), name='product_destroy'),
    # path('products/update/<int:pk>', ProductUpdateApiView.as_view(), name='product_update'),
]
