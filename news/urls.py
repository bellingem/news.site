from django.contrib import admin
from django.urls import path
from .views import* # news_list_view, news_detail_view, contact_view, about_view, local_news_view

appname='news'
urlpatterns = [
    path('', news_list_view, name='news_list'),

    # path('logolist/', logo_list_view, name='logolist'),

    path('contact_us/', contact_view, name='contact_page'),
    path('about_us/', about_view, name='about_page'),
    path('xorij/', local_news_view, name='xorij_page'),
    path('mahalliy/', mahalliy_news_view, name='mahalliy_page'),
    path('sport/', sport_news_view, name='sport_page'),
    path('football/', football_news_view, name='football_page'),
    path('fantexnika/', fantexnika_news_view, name='fantexnika_page'),







    path('<slug>/', news_detail_view, name = 'news_detail'),
]