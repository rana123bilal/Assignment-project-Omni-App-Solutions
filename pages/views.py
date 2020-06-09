from django.shortcuts import get_object_or_404 ,render
from django.http import HttpResponse
from .models import Listing


def index(request):

    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'pages/listing.html' , context)


def search(request):
    query = request.GET['query']
    listings = Listing.objects.filter(movie_name__icontains=query)
    context = {
        'listings': listings
    }
    return render(request, 'pages/search.html', context)
