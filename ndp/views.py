from django.shortcuts import render, get_object_or_404

from ndp.models import Sector


def home(request):
    return render(request, 'index.html', {
        'pagename': 'home',
    })


def about(request):
    return render(request, 'about.html', {
        'pagename': 'about',
    })


def sector(request, slug):
    sector = get_object_or_404(Sector.objects.filter(slug=slug))
    return render(request, 'sector.html', {
        'pagename': 'sector',
        'sector': sector,
    })
