from rest_framework import viewsets, status
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Customer created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": serializer.errors,
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({
            "success": True,
            "message": "List of customers",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    def retrieve(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response({
            "success": True,
            "message": "Customer detail is",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Customer updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
    def destroy(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response({
            "success": True,
            "message": "Customer deleted successfully",
            "data": None
        }, status=status.HTTP_204_NO_CONTENT)