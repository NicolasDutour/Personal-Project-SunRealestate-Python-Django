from django.shortcuts import render
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, surface_choices


def index(request):
    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'surface_choices': surface_choices
    }
    return render(request, 'pages/index.html', context)
