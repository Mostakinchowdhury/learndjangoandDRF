import django_filters
from .models import Comment

class commentFilter(django_filters.FilterSet):
    coment_text = django_filters.CharFilter(field_name="coment_text",lookup_expr='icontains')
    class Meta:
        model = Comment
        fields = ['coment_text']
