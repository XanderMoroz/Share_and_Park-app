from django import forms
from django.contrib.gis.forms import OSMWidget, PointField
from django.forms import ModelForm
from .models import ParkingPlace, Order, AppUser, BankCard

from .utils import subway_station


class ParkingForm(ModelForm):
    """ Форма для создания машино-места"""
    location = PointField(widget=
        OSMWidget(attrs={'map_width': '100%',
                         'map_height': 500,
                         'default_lon': 37.618423,
                         'default_lat': 55.751244,
                         },
                  ))
    title = forms.CharField(widget=
                            forms.TextInput(attrs={"class": "profile__form-input"}))
    description = forms.CharField(widget=
                            forms.Textarea(attrs={"class": "profile__form-input"}))
    pricePerHour = forms.IntegerField(widget=
                                      forms.TextInput(attrs={"class": "profile__form-input"}))


    class Meta:
        """
        В класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля.
        Мы уже делали что-то похожее с фильтрами.
        """
        model = ParkingPlace
        fields = [
            'location',
            'title',
            'description',
            'pricePerHour',
            'readyToRent',
            'subway_station',
            'owner',
            'image',
                ]
        labels = {
            'location': "Расположение на карте",
            'title': "Адрес",
            'description': "Описание",
            'pricePerHour': "Цена за час",
            'readyToRent': "Статус парковочного места",
            'subway_station': "Ближайшее метро",
            'image': "Фотография парковочного места"
        }

        widgets = {'owner': forms.HiddenInput(),
                   # 'readyToRent': forms.HiddenInput()
                   'subway_station': forms.Select(attrs={"class": "profile__form-input"}),
                   'readyToRent' : forms.Select(attrs={"class": "parking-place__form-select"}),
                   }

class OrderForm(ModelForm):
    """Форма для создания брони"""
    class Meta:
        model = Order
        fields = [
            'parkingPlace',
            'orderState',
            'arendator'
                ]

        widgets = {'arendator': forms.HiddenInput(),
                   'orderState': forms.HiddenInput(),
                   'parkingPlace': forms.HiddenInput(),
                   }

class CloseOrderForm(ModelForm):
    """Форма для завершения брони"""
    class Meta:
        model = Order
        fields = [
            'parkingPlace',
            'orderState',
            'arendator'
                ]

        widgets = {'arendator': forms.HiddenInput(),
                   # 'orderState': forms.HiddenInput(),
                   'parkingPlace': forms.HiddenInput(),
                   }

class ProfileForm(ModelForm):
    """Форма для создания профиля"""
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"profile__form-input"}))
    surname = forms.CharField(widget=forms.TextInput(attrs={"class":"profile__form-input"}))
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={"class":"profile__form-input"}))
    # afertaSubmission = forms.BooleanField(widget=forms.BooleanField())
    class Meta:
        model = AppUser
        fields = [
            # 'photo',
            'user',
            'name',
            'surname',
            'phoneNumber',
            # 'afertaSubmission',
        ]

        labels = {
            'name': "Имя",
            'surname': "Фамилия",
            'phoneNumber': "Номер телефона",
        }

        widgets = {'user': forms.HiddenInput(),
                   }

class BankCardForm(ModelForm):
    """Форма для создания банковской карты"""

    card_number = forms.IntegerField(widget=forms.TextInput(attrs={"class": "profile__form-input"}))
    expired_month = forms.CharField(widget=forms.TextInput(attrs={"class": "profile__form-input"}))
    expired_year = forms.CharField(widget=forms.TextInput(attrs={"class": "profile__form-input"}))
    CVC = forms.CharField(widget=forms.TextInput(attrs={"class": "profile__form-input"}))

    class Meta:
        model = BankCard
        fields = [
            'owner',
            'balance',
            'card_number',
            'expired_month',
            'expired_year',
            'CVC'
        ]

        labels = {
            'card_number': "Номер карты",
            'expired_month': "Месяц окончания",
            'expired_year': "Год окончания",
            'CVC': "CVC",
        }


        widgets = {'owner': forms.HiddenInput(),
                   'balance': forms.HiddenInput()}