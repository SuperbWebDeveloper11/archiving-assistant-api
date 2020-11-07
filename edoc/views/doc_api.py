from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics
from ..serializers import DocSerializer
from ..models import Doc
from ..permissions import IsOwnerOrReadOnly
                   

# **************** doc views **************** 
class DocList(generics.ListCreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DocDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
 
