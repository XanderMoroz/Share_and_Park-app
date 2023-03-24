import django_filters
from django_filters import FilterSet, CharFilter, NumberFilter, ChoiceFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from django_filters.widgets import LookupChoiceWidget, RangeWidget
from .models import ParkingPlace

from .utils import subway_station


class MyRangeWidget(django_filters.widgets.RangeWidget):

    def __init__(self, from_attrs=None, to_attrs=None, attrs=None):
        super(MyRangeWidget, self).__init__(attrs)
        if from_attrs:
            self.widgets[0].attrs.update(from_attrs)
        if to_attrs:
            self.widgets[1].attrs.update(to_attrs)


# создаём фильтр
class ParkingPlaceFilter(FilterSet):

    # Filter by lat
    pricePerHour = django_filters.RangeFilter(
        label='Диапазон цены',
        widget=MyRangeWidget(
            from_attrs={'placeholder': 'Минимальная цена'},
            to_attrs={'placeholder': 'Максимальная цена'},
        )
    )

    price__gt = NumberFilter(label='Цена от',
                             field_name='pricePerHour',
                             lookup_expr='gt',
                             )
    price__lt = NumberFilter(label='Цена до',
                             field_name='pricePerHour',
                             lookup_expr='lt',
                             )

    class Meta:
        model = ParkingPlace
        fields = ('readyToRent',
                  # 'pricePerHour',
                  'subway_station',
                  )