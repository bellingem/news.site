from django.http import HttpResponse
from django.shortcuts import render

import news
from .forms import Contactform
from .models import News


def news_list_view(request):
    newslist= News.published.all()
    xorij_news = News.published.filter(category__name = 'Xorij')[:5]
    sport_news = News.published.filter(category__name = 'Sport')[:5]
    mahalliy_news = News.published.filter(category__name = 'Mahalliy yangilikar')[:6]
    football_news = News.published.filter(category__name = 'Football yangiliklar')[:5]
    texnika_news = News.published.filter(category__name = 'Fan- Texnika yangiliklari')[:6]
    newslist1 = News.published.all()[:6]

    context={

        'newslist': newslist,
        'xorij_news':xorij_news,
        'sport_news':sport_news,
        'mahalliy_news':mahalliy_news,
        'football_news':football_news,
        'texnika_news':texnika_news,
        'newslist1':newslist1,


    }

    return render(request, 'index.html', context=context)







def news_detail_view(request,slug):

    new1= News.objects.get(slug= slug )
    yaqin_news= News.objects.filter(category__name = new1.category ).exclude(id=new1.id)[:3]


    context = {
        'news' : new1,
        'yaqin_news':yaqin_news
    }
    return render(request, 'single_page.html', context)


def contact_view(request):
    form = Contactform(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponse('Xabar yuborildi')
    context = {
        'form': form
    }

    return render(request,'contact.html',context=context)


def about_view(request):
    return render(request,'about.html')


def local_news_view(request):
    newslist = News.published.filter(category__name = 'Xorij')

    context = {

        'newslist': newslist,}


    return render(request, 'texno.html', context)
















def mahalliy_news_view(request):
    newslist = News.published.filter(category__name = 'Mahalliy yangilikar')

    context = {

        'newslist': newslist,}


    return render(request, 'texno.html', context)

def sport_news_view(request):
    newslist = News.published.filter(category__name = 'Sport')

    context = {

        'newslist': newslist,}


    return render(request, 'sport.html', context)

def football_news_view(request):
    newslist = News.published.filter(category__name = 'Football yangiliklar')

    context = {

        'newslist': newslist,}


    return render(request, 'football1.html', context)

def fantexnika_news_view(request):
    newslist = News.published.filter(category__name = 'Fan- Texnika yangiliklari')

    context = {

        'newslist': newslist,}


    return render(request, 'fan-texnika.html', context)