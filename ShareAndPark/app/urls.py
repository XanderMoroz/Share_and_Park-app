from django.urls import path
from .views import (
    MainPage,
    ParkingList,
    ParkingDetail,
    CreateParking,
    UpdateParking,
    DeleteParking,

    create_order,

    Profile,
    EditProfile,
    CreateBankCard,
    UpdateBankCard,
    DeleteBankCard,
    UpdateOrder,
)

handler404 = "app.views.handler404"
handler500 = "app.views.handler500"

urlpatterns = [
    path('', MainPage.as_view(), name='welcome page'),                                  # Главная страница
    path('catalog', ParkingList.as_view(), name='parking_list'),                        # Каталог машино-мест
    path('<int:pk>', ParkingDetail.as_view(), name='parking_detail'),                   # Страница машино-места

    path('<int:pk>/create_order', create_order, name='createOrder'),
    # path('create_order', CreateOrder.as_view(), name='create_order'),

    path('create', CreateParking.as_view(), name='create_parking'),                     # Создать машино-место
    path('edit/<int:pk>', UpdateParking.as_view(), name='update_parking'),              # Редактировать машино-место
    path('delete/<int:pk>', DeleteParking.as_view(), name='delete_parking'),            # Удалить машино-место

    path('profile', Profile.as_view(), name='profile'),                                 # Личный кабинет
    path('edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),          # Редактировать профиль
    path('profile/edit_order/<int:pk>', UpdateOrder.as_view(), name='update_order'),    # Завершение аренды

    path('create_bankcard', CreateBankCard.as_view(), name='create_bankcard'),          # Создать карту
    path('edit_bankcard/<int:pk>', UpdateBankCard.as_view(), name='update_bankcard'),   # Редактировать карту
    path('delete_bankcard/<int:pk>', DeleteBankCard.as_view(), name='delete_bankcard'), # Удалить карту
    # path('stop_arenda/<int:pk>', stop_arendation, name='stop_arendation'),
]
