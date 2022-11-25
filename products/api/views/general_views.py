from rest_framework import viewsets
from base.api import GeneralListApiView
from products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer


class MeasureUnitListAPIView(viewsets.ModelViewSet):
    """
    Retorna todas las unidades de medida disponibles

    unidades de medidas
    """
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnitSerializer.Meta.model.objects.all()


class IndicadorListAPIView(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
    queryset = IndicatorSerializer.Meta.model.objects.all()


class CategoryProductListAPIView(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = CategoryProductSerializer.Meta.model.objects.all()



