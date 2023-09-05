from django.shortcuts import render
from .models import Reviews
# Create your views here.

# definig function header to display the student reviews
def header(request):
    object_list = Reviews.object.all()

    return render(request, "reviews/review.html", {"reviews":object_list})

