from rest_framework.serializers import ModelSerializer

from myapp.models import Company


class CompanySerializer(ModelSerializer):
    """Company model serializer"""
    class Meta:
        """Model serializer meta"""
        model = Company
        fields = '__all__'
