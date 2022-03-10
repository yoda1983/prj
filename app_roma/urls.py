from django.urls import path, include
from .views import Index, CourseList, teacher_list, StartGroup, start_work, EduProcces, About, error, robot, pdf_response
app_name = 'app_roma'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('list_courses/', CourseList.as_view(), name='list_courses'),
    path('teachers/', teacher_list, name='teachers'),
    path('near_groups/', StartGroup.as_view(), name='near_groups'),
    path('start_work/', start_work, name='start_work'),
    path('educ/', EduProcces.as_view(), name='edu_procces'),
    path('about/', About.as_view(), name='about'),
    path('error/', error, name='error'),
    path('robots.txt/', robot),
    # path('pdf/', pdf_response, name='pdf_response')
    path('course_program/<int:id>', pdf_response, name='pdf_response'),
]