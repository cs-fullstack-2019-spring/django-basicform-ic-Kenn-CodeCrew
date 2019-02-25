from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import School, People


# Create your views here.
def indexForSchool(request):
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
    # individualSchool = School.objects.get(pk = schoolID)
    individualSchool.students += 1
    individualSchool.save()

    allSchools = School.objects.all()

    context = {
        "allSchool": allSchools
    }

    return render(request, 'SchoolPeopleApp/index.html', context)


def index(request):
    allPeople = People.objects.all()
    context = {
        'allPeople': allPeople
    }
    return render(request, 'SchoolPeopleApp/peopleIndex.html', context)


def helloPerson(request):
    return HttpResponse("Hello " + request.POST["personName"])


def addAStar(request, personID):
    individualPerson = get_object_or_404(People, pk=personID)
    individualPerson.name += "*"
    individualPerson.save()
    return redirect("index")