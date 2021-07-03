#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Bb, Rubric

def index(request):
    #template = loader.get_template('index.html')
    #bbs = Bb.objects.order_by('-published')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context={'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request, 'by_rubric.html', context)









