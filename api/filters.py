from django_filters import FilterSet
from .models import RespiratoryDetection


class RespiratoryDetectionFilter(FilterSet):
    class Meta:
        model = RespiratoryDetection
        fields = ['doctor_id']