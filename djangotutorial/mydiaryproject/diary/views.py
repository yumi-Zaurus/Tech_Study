from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView) :
    template_name = "index.html"


class DiaryCreateView(CreateVirew):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')


class DiaryCreateComplete(TemplateView):
    template_name = 'diary_create_complete.html'