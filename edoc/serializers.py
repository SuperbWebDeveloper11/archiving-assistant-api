from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Company, Doc


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'abbreviation'] 


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ['id', 'title', 'doc_file', 'source', 'destinations'] 



