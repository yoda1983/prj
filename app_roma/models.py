from django.contrib.auth.models import User, AbstractUser
from django.db import models
from datetime import datetime
import re
# Create your models here.


class FeedbackFormModel(models.Model):
    choices_status = (
        ('в обработке', 'в обработке'),
        ('новая заявка', 'новая заявка'),
        ('отказ', 'отказ'),
        ('ожидание подписания договора', 'ожидание подписания договора'),
        ('консультация', 'консультация'),
        ('договор подписан', 'договор подписан'),
    )
    choices_courses = ()
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    number_phone = models.CharField(verbose_name='Номер телефона', blank=False, max_length=15)
    status = models.CharField(max_length=100, choices=choices_status, verbose_name='статус заявки', default='новая заявка')
    courser = models.CharField(max_length=150, verbose_name='Выбранный курс', blank=True)
    name = models.CharField(max_length=20, blank=True, verbose_name='Имя заявителя')
    count = models.IntegerField(verbose_name='Количество заявок от данного номера', default=1)
    number_of_calls = models.IntegerField(verbose_name='количество перезвонов', default=0)
    call_back = models.BooleanField(verbose_name='Перезвонить', default=False)
    student_status = models.BooleanField(verbose_name='Присвоить статус учащегося?', default=False)

    def __str__(self):
        return f"{self.status} {datetime.strftime(self.data,'%m/%d/%Y, %H:%M')}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-data']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.status == 'договор подписан':
            super(FeedbackFormModel, self).save()
            obj = CoursesDescriptionModel.objects.get(name_courses=self.courser)
            obj.not_blocked -= 1
            super(CoursesDescriptionModel, obj).save()
        else:
            super(FeedbackFormModel, self).save()


class CommentsFeedbackModel(models.Model):
    feedback = models.ForeignKey(FeedbackFormModel, on_delete=models.CASCADE, related_name='comment_feedback')
    comment = models.TextField(max_length=150, verbose_name='пояснительный коментарий к звонку', blank=True)
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='время добавления коментария')
    # manager = models.ForeignKey(UsersModel, on_delete=models.PROTECT)

    def __str__(self):
        return f"{datetime.strftime(self.date_pub,'%m/%d/%Y, %H:%M')}"

    def save(self, *args, **kwargs):
        if self.pk is None:
            super(CommentsFeedbackModel, self).save(*args, **kwargs)
            obj = FeedbackFormModel.objects.get(comment_feedback__pk=self.pk)
            obj.number_of_calls += 1
            super(FeedbackFormModel, obj).save(*args, **kwargs)
            
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class SpecializationModel(models.Model):
    name_specialization = models.CharField(max_length=40, verbose_name='Название специализации')

    def __str__(self):
        return f'{self.name_specialization}'

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = ' Специализации'


class CoursesDescriptionModel(models.Model):
    name_spec = models.ForeignKey(SpecializationModel, on_delete=models.PROTECT, related_name='spec')
    name_courses = models.CharField(max_length=150, verbose_name='название курса')
    cost = models.FloatField(verbose_name='Стоимость курса', default=0)
    program_course = models.FileField(upload_to='course_program/')
    description_course = models.TextField(verbose_name='описание курса')
    quantity_lesson = models.IntegerField(verbose_name='Длительность курса', default=0)

    def __str__(self):
        return f'{self.name_courses}'

    class Meta:
        verbose_name = 'Описание Курса'
        verbose_name_plural = 'Описание Курсов'


class CourseDetailModel(models.Model):
    course = models.ForeignKey(CoursesDescriptionModel, on_delete=models.CASCADE, related_name='detail_course')
    detail = models.CharField(max_length=100, verbose_name='Деталь курса')

    def __str__(self):
        return f'{self.detail}'


class AddingCoursesModel(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(CoursesDescriptionModel, on_delete=models.PROTECT, related_name='add_course')
    data_begins = models.DateField(verbose_name='Дата старта', blank=True)
    quantity_place = models.IntegerField(verbose_name='количество мест', default=0)
    booked = models.IntegerField(verbose_name='забронированно мест', default=0)
    not_blocked = models.IntegerField(verbose_name='Осталось мест', default=0)
    unic_number = models.CharField(verbose_name='Уникальный номер', max_length=45)

    def __str__(self):
        return f'{self.course.name_courses}, Свободно мест: {self.quantity_place - self.booked}, Дата старта: {self.data_begins}'

    def save(self):
        obj = AddingCoursesModel.objects.filter(course__name_courses=f'{self.course.name_courses}').last()
        if obj:
            self.unic_number = f'{self.course.name_courses}_{self.data_begins}_' + str(int((obj.unic_number)[-1::])+1)
        else:
            self.unic_number = f'{self.course}_{self.data_begins}_'+'1'
        self.not_blocked = self.quantity_place
        super(AddingCoursesModel, self).save()

    class Meta:
        verbose_name = 'Определенный Курс'
        verbose_name_plural = 'Определенные Курсы'
        ordering = ['id',]


class ITECUserModels(AbstractUser):

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'