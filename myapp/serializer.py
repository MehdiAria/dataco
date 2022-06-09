from rest_framework.serializers import ModelSerializer

from myapp.models import Company, Esg


class CompanySerializer(ModelSerializer):
    """Company model serializer"""
    class Meta:
        """Model serializer meta"""
        model = Company
        fields = '__all__'


class EsgSerializer(ModelSerializer):
    """Esg model serializer"""

    class Meta:
        """Model serializer meta"""
        model = Esg
        fields = '__all__'



