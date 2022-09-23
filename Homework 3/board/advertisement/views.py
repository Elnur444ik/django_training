from django.shortcuts import render


# Create your views here.
from django.views import View


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Усулги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisement/advertisement_list.html', {'advertisements': advertisements})


def advertisement_details(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_details.html', {})


def contacts(request, *args, **kwargs):
    phone_number = '8-800-708-19-45'
    email = 'sales@company.com'
    return render(request, 'advertisement/contacts.html', {'phone_number': phone_number, 'email': email})


def categories(request, *args, **kwargs):
    categories = [
        'Личные вещи',
        'Транспорт',
        'Хобби',
        'Отдых'
    ]
    return render(request, 'advertisement/categories.html', {'categories': categories})


# def regions(request, *args, **kwargs):
#     regions = [
#         'Москва',
#         'Московская область',
#         'Республика Алтай',
#         'Республика Адыгея',
#         'Рязанская область',
#     ]
#     return render(request, 'advertisement/regions.html', {'regions': regions})


class About(View):
    def get(self, request):
        site_name = 'Бесплатные объявления'
        site_description = 'Бесплатные объявления в вашем городе!'
        return render(request, 'advertisement/about.html', {'site_name': site_name,
                                                            'site_description': site_description})


class Regions(View):
    def get(self, request):
        regions = [
            'Москва',
            'Московская область',
            'Республика Алтай',
            'Республика Адыгея',
            'Рязанская область',
        ]

        return render(request, 'advertisement/regions.html', {'regions': regions})


