from django.contrib import admin
from django.views.generic import DetailView

from .models import *
from django.utils.translation import ugettext_lazy as _


class CommentInline(admin.TabularInline):
    model = CommentsFeedbackModel
    fk_name = 'feedback'
    extra = 1
    max_num = 5
    exclude = ('manager',)

    def has_delete_permission(self, request, obj=None):
        return False


class StatusFilter(admin.SimpleListFilter):
    title = _('Статус заявки')
    parameter_name = 'status'

    def lookups(self, request, model_admin):

        return (
            ('в обработке', _('в обработке')),
            ('новая заявка', _('новая заявка')),
            ('отказ', _('отказ')),
            ('ожидание подписания договора', _('ожидание подписания договора')),
            ('консультация', _('консультация'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'в обработке':
            return queryset.filter(status='в обработке')
        if self.value() == 'новая заявка':
            return queryset.filter(status='новая заявка')
        if self.value() == 'отказ':
            return queryset.filter(status='отказ')
        if self.value() == 'ожидание подписания договора':
            return queryset.filter(status='ожидание подписания договора')
        if self.value() == 'консультация':
            return queryset.filter(status='консультация')


@admin.register(FeedbackFormModel)
class Feedback(admin.ModelAdmin):
    fields = (('number_phone', 'name'), ('status', 'courser'), ('call_back', 'student_status'))
    list_display = ['status', 'data', 'count', 'number_of_calls', 'call_back']
    list_filter = ['call_back', StatusFilter]
    search_fields = ['number_phone']
    inlines = [CommentInline]


admin.site.register(SpecializationModel)


class CoursesDescriptionInline(admin.TabularInline):
    model = CourseDetailModel
    fk_name = 'course'
    extra = 1
    max_num = 10


@admin.register(CoursesDescriptionModel)
class CourseAdmin(admin.ModelAdmin):
    fields = (('name_spec', 'name_courses'), 'cost', 'program_course', 'description_course')
    list_display = ['name_courses', 'cost']
    inlines = [CoursesDescriptionInline]


@admin.register(AddingCoursesModel)
class AddingCourseAdmin(admin.ModelAdmin):
    fields = ('course', ('data_begins'), ('quantity_place', 'not_blocked'))
    list_display = ['course', 'data_begins', 'quantity_place', 'booked', 'unic_number']