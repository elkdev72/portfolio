from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Project, Skill, PersonalInfo

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.first()
        context['skills'] = Skill.objects.all().order_by('category', '-proficiency')
        context['projects'] = Project.objects.all()[:3]  # Latest 3 projects
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    ordering = ['order']

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personal_info'] = PersonalInfo.objects.first()
        context['skills'] = Skill.objects.all().order_by('category', '-proficiency')
        return context

def contact(request):
        return render(request, 'contact.html', {
        'personal_info': PersonalInfo.objects.first()
    })