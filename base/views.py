from django.shortcuts import render
from .models import Project, Skill

# Create your views here.


def homePage(request):

    projects = Project.objects.all()
    skillsWithBody = Skill.objects.exclude(body='')
    skillsWithoutBody = Skill.objects.filter(body='')
    context = {'projects': projects,'skillsWithBody': skillsWithBody, 'skillsWithoutBody': skillsWithoutBody}
    return render(request, 'base/home.html', context)
