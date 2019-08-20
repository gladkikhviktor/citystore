from django_filters.rest_framework import DjangoFilterBackend, NumberFilter, FilterSet, ModelChoiceFilter
from rest_framework import viewsets, filters
from main.serializers.price import PriceSerializer
from main.models.price import Price
from main.models import Company
from main.models import Category


class PriceFilter(FilterSet):
    min_price=NumberFilter(field_name='price', lookup_expr='gte')
    max_price=NumberFilter(field_name='price', lookup_expr='lte')
    company = ModelChoiceFilter(queryset=Company.objects.all())
    product__category = ModelChoiceFilter(queryset=Category.objects.all(), label='Category')

    class Meta:
        model = Price
        fields = ['product__name', 'company', 'product__category', 'min_price', 'max_price']

class PriceViewSet(viewsets.ModelViewSet):
    queryset= Price.objects.all()
    serializer_class = PriceSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = PriceFilter
    