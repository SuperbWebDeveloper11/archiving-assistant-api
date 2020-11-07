from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics
from ..serializers import CompanySerializer
from ..models import Company
from ..permissions import IsOwnerOrReadOnly

# **************** company views **************** 
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
                        

