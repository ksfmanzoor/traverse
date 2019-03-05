import os
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.forms.models import model_to_dict
from django.db.models import Q
from sorl.thumbnail import get_thumbnail

from .models import Place, Category, Region
from taggit.models import Tag


def index(request):
    context_dict = {
        'categories': Category.objects.all(),
        'regions': Region.objects.all()
    }

    return render(request, 'places/home.html', context_dict)


def browse(request, region='any', category='any'):
    context_dict = {
        'regions': Region.objects.all(),
        'categories': Category.objects.all(),
        'tagSuggestions': list(Tag.objects.values_list('name', flat=True))
    }

    if region != 'any':
        context_dict['selected_region'] = region

    if category != 'any':
        context_dict['selected_category'] = category

    return render(request, 'places/browse.html', context_dict)


def api(request):
    query = Q()

    categories = json.loads(request.GET.get('categories', '[]'))
    if len(categories) > 0:
        query &= Q(category__name__in=categories)

    regions = json.loads(request.GET.get('regions', '[]'))
    if len(regions) > 0:
        query &= Q(region__name__in=regions)

    tags = json.loads(request.GET.get('tags', '[]'))
    tags = filter(None, tags)
    if len(tags) > 0:
        query &= Q(tags__name__in=tags)

    results = Place.objects.filter(query).distinct()

    places = [model_to_dict(result, fields=['name', 'title', 'subtitle']) for result in results]
    thumbnails = [get_thumbnail('covers/' + place.coverImage, '400x400', crop='center', quality=99).url for place in results]

    return HttpResponse(json.dumps({'places': places, 'thumbnails': thumbnails}))


def weather(request):
    return render(request, 'places/weather.html')


def details(request, name):
    place_name = name
    place = Place.objects.get(name=place_name)
    media_directory = settings.MEDIA_ROOT

    images = []
    for filename in os.listdir(os.path.join(media_directory, 'gallerys', place_name)):
        images.append('gallerys/' + place_name + '/' + filename)

    context_dict = {
        'place': place,
        'gallery': images,
    }

    return render(request, 'places/details.html', context_dict)
