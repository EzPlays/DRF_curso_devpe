from rest_framework import generics
from base.api import GeneralListApiView
from products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer


class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class IndicadorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer


class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer



