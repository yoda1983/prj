from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.template.response import TemplateResponse, SimpleTemplateResponse
from django.urls import reverse
import re

from django.views.generic.detail import SingleObjectMixin

from .forms import NumberPhone
from .models import *
from .middleware import form_middleweare
from django.views.generic.base import TemplateView, ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ModelFormMixin
from django.views.generic.edit import CreateView


# Create your views here.


def robot(request):
    lines = [
        "User - agent: *",
        "Disallow: /",
        "Host: http: // 18.198.111.209",
    ]
    return HttpResponse(content_type='text/plain', content='\n'.join(lines))


class GenericClass(CreateView):
    form_class = NumberPhone

    def get_form(self, form_class=None, con=None):
        self.object = super().get_form(form_class)
        return self.object

    def post(self, request, *args, **kwargs):
        form = NumberPhone(request.POST)
        if re.fullmatch(r"^((80|\+375)?)(25|33|44|29)(\d{7})$", form.data.get('number_phone')):
            return self.form_valid(form, request)
        else:
            return render(request, self.template_name, {'con': 2})

    def form_valid(self, form, request):
        try:
            obj = FeedbackFormModel.objects.get(number_phone=form.data.get('number_phone'))
            if obj.count <= 5:
                obj.count += 1
                obj.save()
                return render(self.request, self.template_name, {'con': 1})
            else:
                return render(self.request, self.template_name, {'con': 3})
        except:
            form.save()
            return render(self.request, self.template_name, {'con': 1})


class Index(GenericClass):
    template_name = 'main.html'
    success_url = '/'


class CourseList(GenericClass):
    template_name = 'course_page.html'
    success_url = '/list_courses/'
    extra_context = {'obj': SpecializationModel.objects.all()}
    print(extra_context)


def teacher_list(request):
    return render(request, 'teacher.html')


class StartGroup(GenericClass):
    template_name = 'start__group.html'
    success_url = '/near_groups/'


def start_work(request):
    return render(request, 'startwork.html')


class EduProcces(GenericClass):
    template_name = 'education_process.html'
    success_url = '/educ/'


class About(GenericClass):
    template_name = 'about__itec.html'
    success_url = '/about/'


def error(request):
    return render(request, 'error.html')


# def pdf_response(request):
#     return FileResponse(open('media/result.pdf', 'rb'))
def pdf_response(request, id):
    try:
        obj = CoursesDescriptionModel.objects.get(id=id)
        return FileResponse(open('media/' + str(obj.program_course), 'rb'))
    except BaseException as e:
        print(e)
        return render(request, 'main.html')
