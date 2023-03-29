from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import ParkingPlace, Order, AppUser, BankCard, Сheque
from .forms import ParkingForm, OrderForm, CloseOrderForm, ProfileForm, BankCardForm
from .filters import ParkingPlaceFilter
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
import folium
from .utils import custom_popup_render
from django.contrib.auth import authenticate



# Create your views here.

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline
from django.contrib.postgres.search import TrigramSimilarity


class CSRFExemptMixin(object):
   @method_decorator(csrf_exempt)
   def dispatch(self, *args, **kwargs):
       return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)



class MainPage(ListView):
    """Представление главной страницы"""
    model = ParkingPlace
    # ordering = '-creation_date'
    template_name = 'main.html'                 # Относительный адрес шаблона
    context_object_name = 'demo_place_list'             # Имя для обращения в контексте



class ParkingList(ListView):
    """Представление каталога"""
    model = ParkingPlace                                # Имя модели
    template_name = 'parking/catalog.html'              # Относительный адрес шаблона
    context_object_name = 'parking_list'                # Имя для обращения в контексте
    ordering = ['pricePerHour']                         # Сортировка по убыванию цены
    paginate_by = 1                                     # Поставим постраничный вывод в один элемент


    # забираем отфильтрованные объекты переопределяя метод get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # search
        # search_res = ParkingPlace.objects.all()
        user_search_request = self.request.GET.get("query")

        if user_search_request:
            search_res = ParkingPlace.objects.annotate \
                (similarity=TrigramSimilarity \
                    ('title', user_search_request), ).filter \
                (similarity__gt=0.3).order_by('-similarity')
        else:
            search_res = None

        # вписываем наш фильтр в контекст
        filter_result = ParkingPlaceFilter(self.request.GET, queryset=self.get_queryset())
        # user_search_request = self.request.GET.get("query")
        # if filter_result:
        context['filter'] = filter_result
        context['search_res'] = search_res

        # вписываем карту "folium" в контекст
        figure = folium.Figure()
        mosckow_map = folium.Map(
            location=[55.751244, 37.618423],
            zoom_start=10,
            tiles='openstreetmap',  # ,'Stamen Terrain'
            # width='100%',
            # height='100%',
        )
        mosckow_map.add_to(figure) # устанавливаем фокус карты

        if not self.request.user.is_authenticated:
            print('не авторизован s')
            if search_res:
                print('есть поисковой запрос')
                for place in search_res:
                    place_location = [place.location.coords[1], place.location.coords[0]]

                    # устанавливаем карточку машино-места
                    htmlcode = custom_popup_render(place, user_auth=False)

                    tooltip = f"{place.readyToRent}!"
                    # добавляем машино-место на карту
                    folium.Marker(location=place_location,
                                  popup=htmlcode,
                                  # icon=place_icon,
                                  tooltip=tooltip
                                  ).add_to(mosckow_map)

                # конвертируем данные в html
                map_html = mosckow_map._repr_html_()
                context["map"] = map_html
            else:
                print('нет поискового запроса но есть фильтрация')
                for place in filter_result.qs:
                    place_location = [place.location.coords[1], place.location.coords[0]]

                    # устанавливаем карточку машино-места
                    htmlcode = custom_popup_render(place, user_auth=False)

                    tooltip = f"{place.readyToRent}!"
                    # добавляем машино-место на карту
                    folium.Marker(location=place_location,
                                  popup=htmlcode,
                                  # icon=place_icon,
                                  # tooltip=tooltip
                                  ).add_to(mosckow_map)

                # конвертируем данные в html
                map_html = mosckow_map._repr_html_()
                context["map"] = map_html
        else:
            print('авторизован')
            if search_res:
                print('есть поисковой запрос')
                for place in search_res:
                    place_location = [place.location.coords[1], place.location.coords[0]]

                    # устанавливаем карточку машино-места
                    htmlcode = custom_popup_render(place, user_auth=True)

                    tooltip = f"{place.readyToRent}!"
                    # добавляем машино-место на карту
                    folium.Marker(location=place_location,
                                  popup=htmlcode,
                                  # icon=place_icon,
                                  tooltip=tooltip
                                  ).add_to(mosckow_map)

                # конвертируем данные в html
                map_html = mosckow_map._repr_html_()
                context["map"] = map_html
            else:
                print('нет поискового запроса но есть фильтрация')
                for place in filter_result.qs:
                    place_location = [place.location.coords[1], place.location.coords[0]]
                    # устанавливаем карточку машино-места
                    htmlcode = custom_popup_render(place, user_auth=True)

                    tooltip = f"{place.readyToRent}!"
                    # добавляем машино-место на карту
                    folium.Marker(location=place_location,
                                  popup=htmlcode,
                                  # icon=place_icon,
                                  tooltip=tooltip
                                  ).add_to(mosckow_map)

                map_html = mosckow_map._repr_html_()
                context["map"] = map_html

        return context

class ParkingDetail(CSRFExemptMixin, DetailView, CreateView, LoginRequiredMixin):
    """Представление машино-места"""
    model = ParkingPlace
    template_name = 'parking/parking_detail.html'       # Относительный адрес шаблона
    context_object_name = 'parking_detail'              # Имя для обращения в контексте
    form_class = OrderForm                              # Имя формы

    def get_initial(self):
        # """Переопределение функции для автозаполнения полей 'arendator' и 'parkingPlace' """
        # if self.request.user == 1:
        initial = super().get_initial()
        user = self.request.user
        parkingPlace = ParkingPlace.objects.get(id=self.kwargs['pk'])
        profile = AppUser.objects.get(user=user)
        initial['arendator'] = profile
        initial['parkingPlace'] = parkingPlace

        return initial

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # Добавим в контекст банковские карты текущего пользователя.
        current_user = self.request.user
        user_profile = AppUser.objects.get(user=current_user)
        user_cards = BankCard.objects.filter(owner=user_profile)
        context['user_cards'] = user_cards
        # Добавим в контекст название станции метро.
        current_parkingPlace = ParkingPlace.objects.get(id=self.kwargs['pk'])
        current_subway_station = current_parkingPlace.subway_station
        current_station_name = current_parkingPlace.get_subway_station_display()
        # Добавим в контекст название станции метро машино-места.
        context['current_station'] = current_station_name
        # Добавим в контекст ближайшие к станции метро машино-места, за исключением текущего.
        places_around = ParkingPlace.objects.filter(subway_station=current_subway_station).exclude(id=self.kwargs['pk'])
        context['places_around'] = places_around

        return context

class CreateParking(CSRFExemptMixin, CreateView, LoginRequiredMixin):
    """Представление для создания машино-места."""
    model = ParkingPlace                                # Имя модели
    template_name = 'parking/create_parking.html'       # Относительный адрес шаблона
    form_class = ParkingForm                            # Имя формы

    def get_initial(self):
        """Переопределение функции для автозаполнения поля "автор объявления" """
        initial = super().get_initial()
        user = self.request.user
        initial['owner'] = user
        return initial

class UpdateParking(CSRFExemptMixin, UpdateView, LoginRequiredMixin):
    """Представление для редактирования машино-места."""
    template_name = 'parking/edit_parking.html'         # Относительный адрес шаблона
    form_class = ParkingForm                            # Имя формы
    context_object_name = 'my_parkingPlace'

    def get_object(self, **kwargs):
        """Метод get_object мы используем вместо queryset,
        чтобы получить информацию об объекте, который мы собираемся редактировать"""
        id = self.kwargs.get('pk')
        return ParkingPlace.objects.get(pk=id)

class DeleteParking(CSRFExemptMixin, DeleteView, LoginRequiredMixin):
    """Представление для удаления машино-места."""
    template_name = 'parking/delete_parking.html'       # Относительный адрес шаблона
    queryset = ParkingPlace.objects.all()               # Кварисет (набор) объектов
    success_url = reverse_lazy('profile')               # Перенаправление после удаления

class Profile(CSRFExemptMixin, TemplateView):
    """Представление профиля пользователя."""
    model = User                                        # Имя модели
    template_name = 'profile/profile.html'              # Относительный адрес шаблона
    form_class = ProfileForm                            # Имя формы

    def get_initial(self):
        """Переопределение функции для автозаполнения поля 'user' """
        initial = super().get_initial()
        user = self.request.user
        initial['user'] = user
        return initial

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим пользователя'.
        user = self.request.user
        # Добавим в контекст профиль пользователя
        profile = AppUser.objects.get(user=user)
        context['profile'] = profile
        # Добавим в контекст карты пользователя
        myCards = BankCard.objects.filter(owner=profile)
        context['my_cards'] = myCards
        # Добавим в контекст машино-места пользователя
        myParkingPlaces = ParkingPlace.objects.filter(owner=profile)
        context['my_places'] = myParkingPlaces
        # Добавим в контекст брони маниноместа пользователя
        myBooking = Order.objects.filter(arendator=profile, orderState='ON')
        context['my_orders'] = myBooking
        # Добавим в контекст доходы пользователя
        myProfits = Сheque.objects.filter(beneficiary=profile)
        context['my_profits'] = myProfits
        # Добавим в контекст расходы пользователя
        myPayments = Сheque.objects.filter(payer=profile)
        context['my_payments'] = myPayments

        return context

class EditProfile(CSRFExemptMixin, UpdateView):
    """Представление для редактирования профиля пользователя."""
    template_name = 'profile/edit_profile.html'         # Относительный адрес шаблона
    form_class = ProfileForm                            # Имя формы
    context_object_name = 'current_profile'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return AppUser.objects.get(pk=id)

@csrf_exempt
def create_order(request, **kwargs):
    """Функция создания брони машиноместа."""
    current_parking_place = ParkingPlace.objects.get(pk=kwargs['pk'])
    current_user = request.user
    current_user_profile = AppUser.objects.get(user=current_user)

    Order.objects.create(parkingPlace=current_parking_place,
                         arendator=current_user_profile)

class UpdateOrder(CSRFExemptMixin, UpdateView):
    """Представление для завершения брони машиноместа."""
    template_name = 'profile/edit_order.html'           # Относительный адрес шаблона
    form_class = CloseOrderForm                         # Имя формы

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Order.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим экземпляр текущей аренды парковки.
        this_order = Order.objects.get(pk=self.kwargs.get('pk'))
        context['this_order'] = this_order
        rent_time = timezone.now() - this_order.creation_date   # вычисляем время аренды
        # К словарю добавим часы текущей аренды парковки.
        rent_hours = rent_time.seconds // 3600
        print(rent_hours)
        context['rent_hours'] = int(rent_hours)
        # К словарю добавим минуты текущей аренды парковки.
        rent_minutes = rent_time.seconds % 3600 // 60           # вычисляем минуты аренды
        context['rent_minutes'] = rent_minutes
        print(rent_minutes)
        price_per_hour = this_order.parkingPlace.pricePerHour   # извлекаем стоимость аренды за час
        price_hours = (rent_hours * price_per_hour)             # вычисляем стоимость арендованных часов
        price_per_min = (price_per_hour / 60)
        price_minutes = + (price_per_min * rent_minutes)        # вычисляем стоимость арендованных минут
        total_price = int(price_hours + price_minutes)          # вычисляем полную стоимость аренды
        context['total_price'] = total_price

        return context




# def stop_arendation(request, **kwargs):
#     """Функция завершения брони машиноместа."""
#     order = Order.objects.get(pk=kwargs['pk'])
#     order.orderState =  'OFF'
#     order.save(update_fields=["orderState"])
#
#     return redirect(request.META.get('HTTP_REFERER', '/'))

class CreateBankCard(CSRFExemptMixin, CreateView, LoginRequiredMixin):
    """Представление для создания банковской карты."""
    model = BankCard                                    # Имя модели
    template_name = 'bankcard/create_bankcard.html'      # Относительный адрес шаблона
    form_class = BankCardForm                           # Имя формы

    def get_initial(self):
        """Переопределение функции для автозаполнения поля owner"""
        initial = super().get_initial()
        user = self.request.user
        initial['owner'] = user
        return initial

class UpdateBankCard(CSRFExemptMixin, UpdateView, LoginRequiredMixin):
    """Представление для редактирования банковской карты."""
    template_name = 'bankcard/edit_bankcard.html'         # Относительный адрес шаблона
    form_class = BankCardForm                            # Имя формы
    context_object_name = 'my_bankcard'

    def get_object(self, **kwargs):
        """Метод get_object мы используем вместо queryset,
        чтобы получить информацию об объекте, который мы собираемся редактировать"""
        id = self.kwargs.get('pk')
        return BankCard.objects.get(pk=id)

class DeleteBankCard(DeleteView, LoginRequiredMixin):
    """Представление для удаления банковской карты."""
    template_name = 'bankcard/delete_bankcard.html'      # Относительный адрес шаблона
    queryset = BankCard.objects.all()                    # Кварисет (набор) схожих объектов
    success_url = reverse_lazy('profile')                # Перенаправление после удаления

@csrf_exempt
def handler404(request, exception):
    return render(request, '404.html', status=404)
@csrf_exempt
def handler500(request):
    return render(request, '500.html', status=404)

@csrf_exempt
def new_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('profile'))
        else:
            messages.error(request, 'username or password not correct')
            return redirect(reverse('new_login'))


    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
