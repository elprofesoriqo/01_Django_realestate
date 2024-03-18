from django.shortcuts import render
from .models import Listing
# Create your views here.
def listing_list(request):
    listings = Listing.objects.all()
    context={
        "listings": listings
    }
    return render(request, "listings.html", context)

def listing_retrive(request, pk):
    listing= Listing.objects.get(id=pk)
    context = {
        "lisitng": listing
    }

    return render(request, "lisiting.html", context)
