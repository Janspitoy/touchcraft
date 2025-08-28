from django.http import HttpResponse
from django.shortcuts import render
from .models import Service, Project
from django.db.models import Q


def home(request):
    """Главная страница"""
    services = Service.objects.all()
    projects = Project.objects.all()[:3]  # можно Meta.ordering использовать
    return render(request, 'main/home.html', {
        'services': services,
        'projects': projects,
    })


def contacts(request):
    """Страница контактов"""
    return render(request, 'main/contacts.html')


def services(request):
    """Список услуг"""
    services_list = Service.objects.all()
    return render(request, 'main/services.html', {
        'services': services_list
    })


def portfolio(request):
    """Портфолио"""
    # Фильтр для игр
    game_filter = (
        Q(title__icontains="игра") |
        Q(description__icontains="игра") |
        Q(title_en__icontains="game") |
        Q(description_en__icontains="game") |
        Q(title_es__icontains="juego") |
        Q(description_es__icontains="juego") |
        Q(title_uk__icontains="гра") |
        Q(description_uk__icontains="гра")
    )

    show_all = request.GET.get("all") == "1"  # при нажатии на кнопку ?all=1

    if show_all:
        # Все проекты
        projects_list = Project.objects.exclude(game_filter)
        games_list = Project.objects.filter(game_filter)
    else:
        # Последние 3 проекта и 3 игры
        projects_list = Project.objects.exclude(game_filter)[:3]
        games_list = Project.objects.filter(game_filter)[:3]

    return render(request, 'main/portfolio.html', {
        'projects': projects_list,
        'games': games_list,
        'show_all': show_all
    })

def app_ads_txt(request):
    return HttpResponse(
        "google.com, pub-4411114348896099, DIRECT, f08c47fec0942fa0",
        content_type="text/plain"
    )