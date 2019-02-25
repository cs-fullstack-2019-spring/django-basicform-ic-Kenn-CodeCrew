from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("printStudent/", views.printStudent, name="printStudent"),
    path("<int:schoolID>/addStudentToSchool/", views.addStudentToSchool, name="addStudentToSchool"),

    path("helloPerson/", views.helloPerson, name="helloPerson"),
    path("addAStar/<int:personID>", views.addAStar, name="addAStar"),
]