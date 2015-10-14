from random import shuffle

from django.shortcuts import render, get_object_or_404

from ndp.models import Sector, Organisation


def home(request):
    sectors = list(Sector.objects.all())
    shuffle(sectors)

    return render(request, 'index.html', {
        'pagename': 'home',
        'sectors': sectors,
    })


def about(request):
    sectors = list(Sector.objects.all())
    shuffle(sectors)

    return render(request, 'about.html', {
        'pagename': 'about',
        'sectors': sectors,
    })


def sector(request, slug):
    sector = get_object_or_404(Sector.objects.filter(slug=slug))

    sectors = list(Sector.objects.all())
    shuffle(sectors)

    return render(request, 'sector.html', {
        'pagename': 'sector',
        'sector': sector,
        'sectors': sectors,
    })


def organisation(request, org_id):
    organisation = get_object_or_404(Organisation.objects.filter(id=org_id))

    sectors = list(Sector.objects.all())
    shuffle(sectors)

    return render(request, 'organisation.html', {
        'pagename': 'contributor',
        'organisation': organisation,
        'sectors': sectors,
    })
