from django.shortcuts import render
from .models import Movie, Collection, Genres, Premiere

def main_page(request):
    collections = Collection.objects.all()
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    premieres = Premiere.objects.all()

    context = {
        'movies': movies,
        'collections': collections,
        'genres': genres,
        'premieres': premieres
    }

    return render(request, 'index.html', context)