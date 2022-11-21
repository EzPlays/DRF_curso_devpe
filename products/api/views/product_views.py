from base.api import GeneralListApiView
from products.api.serializers.product_serializer import ProductSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state = True)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    def list(self, request):
        print('List')
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(product_serializer.data, status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'product created succesfully'}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status.HTTP_200_OK)
            return Response(product_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'product deleted succesfully'}, status.HTTP_200_OK)
        return Response({'error': 'Not exist product'}, status.HTTP_400_BAD_REQUEST)
    

# class ProductListApiView(GeneralListApiView):
#     serializer_class = ProductSerializer

# class ProductCreateApiView(generics.CreateAPIView):
#     serializer_class = ProductSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'product created succesfully'}, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ProductListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    queryset = ProductSerializer.Meta.model.objects.filter(state = True)

    # def get_queryset(self):
    #     pass

    # def get(self, request):
    #     pass

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'product created succesfully'}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    def patch(self, request, pk= None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status.HTTP_200_OK)
        return Response({'error': 'Not exist product'}, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status.HTTP_200_OK)
            return Response(product_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'product deleted succesfully'}, status.HTTP_200_OK)
        return Response({'error': 'Not exist product'}, status.HTTP_400_BAD_REQUEST)

# class ProductRetrieveApiView(generics.RetrieveAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state = True)
    

# class ProductDestroyApiView(generics.DestroyAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state = True)

#     def delete(self, request, pk=None):
#         product = self.get_queryset().filter(id = pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message':'product deleted succesfully'}, status.HTTP_200_OK)
#         return Response({'error': 'Not exist product'}, status.HTTP_400_BAD_REQUEST)


# class ProductUpdateApiView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self, pk):
#         return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

#     def patch(self, request, pk= None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk))
#             return Response(product_serializer.data, status.HTTP_200_OK)
#         return Response({'error': 'Not exist product'}, status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response(product_serializer.data, status.HTTP_200_OK)
#             return Response(product_serializer.errors, status.HTTP_400_BAD_REQUEST)



