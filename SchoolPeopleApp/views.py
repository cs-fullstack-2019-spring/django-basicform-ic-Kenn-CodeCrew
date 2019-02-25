from django.shortcuts import render, get_object_or_404
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


def printStudent(request):
    print(request.POST)
    print(request.POST["studentName"])
    print(request.POST["studentAge"])
    return HttpResponse("Hello " + request.POST["studentName"])


def addStudentToSchool(request, schoolID):
    individualSchool = get_object_or_404(School, pk=schoolID)
    individualSchool.students += 1
    individualSchool.save()

    allSchools = School.objects.all()

    context = {
        "allSchool": allSchools
    }

    return render(request, 'SchoolPeopleApp/index.html', context)