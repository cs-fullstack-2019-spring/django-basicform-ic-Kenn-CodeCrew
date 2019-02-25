from django.shortcuts import render
from django.http import HttpResponse
from .models import School


# Create your views here.
def index(request):
    allSchools = School.objects.all()
    context = {
        "allSchool": allSchools
    }
    return render(request, 'SchoolPeopleApp/index.html', context)
    # return HttpResponse("Test URL I hope this works")