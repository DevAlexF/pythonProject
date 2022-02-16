from typing import Union

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import *


# a = Zodiac.objects.all()

# print(a[0].name)
# print(a[0].information)
# print(a[0].name, a[0].information)

# b = a[0].name, a[0].information
# c = a[1].name, a[2].information
# d = a[2].name, a[2].information
# e = a[3].name, a[3].information
# print(b+c+d+e)

a = Zodiac.objects.all()
b = []
for x in range(0, len(a)):
    b.append(a[x].name)
    b.append(a[x].information)
print(b)
zodiac_dict = {b[i]: b[i + 1] for i in range(0, len(b), 2)}
print()
print(zodiac_dict)

print()
print('hi')
print('hello')

# zodiac_dict = {
#     'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
#     'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
#     'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
#     'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
#     'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
#     'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
#     'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
#     'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
#     'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
#     'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
#     'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
#     'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
# }

def index(request):  # 3 Создаем функцию для меню
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f"<li> <a href ='{redirect_path}'>{sign.title()}</a></li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str) -> Union[HttpResponse, HttpResponseNotFound]:
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
