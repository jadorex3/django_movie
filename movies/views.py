from django.shortcuts import render
from django.views.generic.base import View

from movies.models import Movie


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list': movies})


class MovieDetailView(View):
    """Детальное описание фильма"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})