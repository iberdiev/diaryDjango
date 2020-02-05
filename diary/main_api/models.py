from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
import os, logging, platform
from .loggers import (creations_logger, updates_logger, deletions_logger)


class CustomUser(AbstractUser):
    db = 'default'
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    user_role = models.IntegerField(null=True)
    created_date = models.DateTimeField('date_created', auto_now_add = True, null=True)
    phoneNumber = models.CharField(default='', max_length=255)
    codeToResetPassword = models.IntegerField(null=True)
    class Meta:
       verbose_name_plural = "1. Пользователи"

    def __str__(self):
        return self.username

class Teacher(models.Model):
    db = 'default'
    teacherName = models.CharField(max_length = 100)
    schoolID = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null = True, related_name='teachers')
    teacherID = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name='mainTeacher')
    class Meta:
       verbose_name_plural = "2. Учителя"
    # def save_model(self, request, obj, form, change):
    #     obj.schoolID = request.user
    #     super().save_model(request, obj, form, change)

    def __str__(self):
        return self.teacherName


class Cohort(models.Model):
    db = 'default'
    school_creator = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='cohorts')
    mainTeacherID = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='mainCohorts')
    class_name = models.CharField(max_length = 100)
    jkitepClassID = models.IntegerField(null=True, unique=True)
    class Meta:
       verbose_name_plural = "3. Классы"
    def __str__(self):
        return self.class_name

class Student(models.Model):
    db = 'default'
    studentName = models.CharField(max_length = 100)
    cohort = models.ForeignKey(Cohort, on_delete=models.SET_NULL, null=True, related_name='students')
    parent = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL, related_name='child')
    phoneNumber = models.CharField(default='', max_length=255)
    def __str__(self):
        return self.studentName
    class Meta:
       verbose_name_plural = "4. Студенты"

    # def save_post(sender, instance, **kwargs):
    #     school.
    #     teacher = Teacher(teacherName=instance.name,schoolID=)
    #     print(instance.name)
    # post_save.connect(save_post, sender=CustomUser)

class Subject(models.Model):
    db = 'default'
    subjectName = models.CharField(max_length = 100)
    cohortID = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='subjects')
    teacherID = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='subjects', null=True)
    def __str__(self):
        return  '%s - %s' % (self.cohortID, self.subjectName)
    class Meta:
       verbose_name_plural = "5. Предметы"

class Timetable(models.Model):
    db = 'default'
    subjectID = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable')
    cohortID = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='timetable')
    date = models.DateField(null=True)
    startTime = models.TimeField(null=True)
    endTime = models.TimeField(null=True)
    homework = models.CharField(max_length = 100, default='', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='timetable', null=True)
    class Meta:
       ordering = ('date',)
       verbose_name_plural = "6. Расписание уроков"
    def __str__(self):
        return  '%s - %s' % (self.date, self.subjectID)


class regularGrade(models.Model):
    db = 'default'
    lesson = models.ForeignKey(Timetable, on_delete=models.SET_NULL, related_name='regularGrades', null=True)
    studentID = models.ForeignKey(Student, on_delete=models.SET_NULL, related_name='regularGrades', null=True)
    teacherID = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    mark = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(2)])
    TYPE_CHOICES = (
        (1, 'Первая четверть'),
        (2, 'Вторая четверть'),
        (3, 'Третья четверть'),
        (4, 'Четвертая четверть'),
        (5, 'Итог'),
        (6, 'Повседневная оценка'),
    )
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=6)
    class Meta:
       verbose_name_plural = "7. Обычные оценки"
    def __str__(self):
        return  '%s - %s' % (self.lesson, self.studentID)

class finalGrade(models.Model):
    db = 'default'
    subjectID = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    studentID = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='finalGrades')
    mark = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(2)])
    TYPE_CHOICES = (
        (1, 'Первая четверть'),
        (2, 'Вторая четверть'),
        (3, 'Третья четверть'),
        (4, 'Четвертая четверть'),
        (5, 'Итог'),
    )
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    class Meta:
       verbose_name_plural = "8. Итоговые оценки"
    def __str__(self):
        return  '%s - %s' % (self.subjectID, self.studentID)

class ModTrackerDjango(models.Model):
    db = 'default'
    prevalue = models.CharField(max_length = 250, default = '')
    postvalue = models.CharField(max_length = 250)
    model = models.CharField(max_length = 250)
    attribute = models.CharField(max_length = 250)
    action = models.CharField(max_length = 250)
    def __str__(self):
        return "%s: %s - %s - %s -> %s" %(self.action, self.model, self.attribute, self.prevalue, self.postvalue)


class JkitepSchools(models.Model):
    db = 'test'
    schoolsid = models.IntegerField(primary_key=True)
    schools_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    school_code = models.CharField(max_length=100, blank=True, null=True)
    found_school = models.DateField(blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    work_phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    region_id = models.CharField(max_length=100, blank=True, null=True)
    balance = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    school_number = models.CharField(max_length=400, blank=True, null=True)
    type_school = models.CharField(max_length=200, blank=True, null=True)
    type_ownership = models.CharField(max_length=200, blank=True, null=True)
    language_instruction = models.CharField(max_length=200, blank=True, null=True)
    school_address = models.CharField(max_length=200, blank=True, null=True)
    school_named = models.CharField(max_length=100, blank=True, null=True)
    region_school_id = models.CharField(max_length=100, blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    startbalance = models.CharField(max_length=100, blank=True, null=True)
    okpo = models.CharField(max_length=100, blank=True, null=True)
    fioadding = models.CharField(max_length=100, blank=True, null=True)
    posadding = models.CharField(max_length=100, blank=True, null=True)
    workingcount = models.IntegerField(blank=True, null=True)
    staffplancount = models.IntegerField(blank=True, null=True)
    stafffactcount = models.IntegerField(blank=True, null=True)
    staffwomcount = models.IntegerField(blank=True, null=True)
    staff5count = models.IntegerField(blank=True, null=True)
    staff1115count = models.IntegerField(blank=True, null=True)
    staff15count = models.IntegerField(blank=True, null=True)
    staffcer5tcount = models.IntegerField(blank=True, null=True)
    staffcert1count = models.IntegerField(blank=True, null=True)
    staffhiedcount = models.IntegerField(blank=True, null=True)
    staffneedcount = models.IntegerField(blank=True, null=True)
    staffmedcount = models.IntegerField(blank=True, null=True)
    mobadding = models.CharField(max_length=100, blank=True, null=True)
    mailadding = models.CharField(max_length=100, blank=True, null=True)
    staff510count = models.IntegerField(blank=True, null=True)
    totalsquare = models.CharField(max_length=100, blank=True, null=True)
    edusquare = models.CharField(max_length=100, blank=True, null=True)
    othsquare = models.CharField(max_length=100, blank=True, null=True)
    rentsquare = models.CharField(max_length=100, blank=True, null=True)
    buildingstate = models.CharField(max_length=100, blank=True, null=True)
    usestate = models.CharField(max_length=100, blank=True, null=True)
    sewerage = models.CharField(max_length=20, blank=True, null=True)
    hotwater = models.CharField(max_length=20, blank=True, null=True)
    toilets = models.CharField(max_length=20, blank=True, null=True)
    drinkwater = models.CharField(max_length=20, blank=True, null=True)
    washbasins = models.CharField(max_length=20, blank=True, null=True)
    spectoilet = models.CharField(max_length=20, blank=True, null=True)
    lifts = models.CharField(max_length=20, blank=True, null=True)
    classeson1 = models.CharField(max_length=20, blank=True, null=True)
    medpersons = models.CharField(max_length=20, blank=True, null=True)
    specedupers = models.CharField(max_length=20, blank=True, null=True)
    elecliblary = models.CharField(max_length=20, blank=True, null=True)
    compcount = models.IntegerField(blank=True, null=True)
    workcompcount = models.IntegerField(blank=True, null=True)
    intcompcount = models.IntegerField(blank=True, null=True)
    projector = models.CharField(max_length=20, blank=True, null=True)
    copierprinter = models.CharField(max_length=20, blank=True, null=True)
    inttype = models.CharField(max_length=100, blank=True, null=True)
    intspeed = models.CharField(max_length=100, blank=True, null=True)
    intmanagem = models.CharField(max_length=20, blank=True, null=True)
    intinallclas = models.CharField(max_length=20, blank=True, null=True)
    availeverywifi = models.CharField(max_length=20, blank=True, null=True)
    inttv = models.CharField(max_length=20, blank=True, null=True)
    physicslab = models.CharField(max_length=20, blank=True, null=True)
    chemistrylab = models.CharField(max_length=20, blank=True, null=True)
    biologylab = models.CharField(max_length=20, blank=True, null=True)
    hotfood = models.CharField(max_length=20, blank=True, null=True)
    booklibraryc = models.IntegerField(blank=True, null=True)
    tbooklibraryc = models.IntegerField(blank=True, null=True)
    pandus = models.CharField(max_length=20, blank=True, null=True)
    balance_sum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schools'

class JkitepSchoolclasses(models.Model):
    db = 'test'
    schoolclassesid = models.IntegerField(primary_key=True)
    school_classes_no = models.CharField(max_length=100, blank=True, null=True)
    class_id = models.CharField(max_length=100, blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    startbalance = models.CharField(max_length=100, blank=True, null=True)
    lang_instruc_class = models.CharField(max_length=200, blank=True, null=True)
    yyyy = models.CharField(max_length=100, blank=True, null=True)
    balance_sum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolclasses'


class JkitepSchoolstaff(models.Model):
    db = 'test'
    schoolstaffid = models.IntegerField(primary_key=True)
    school_staff_no = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    pin_con = models.CharField(max_length=100, blank=True, null=True)
    mobile_phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    position_school_staff = models.CharField(max_length=300, blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    user_employee_id = models.CharField(max_length=100, blank=True, null=True)
    status_users = models.CharField(max_length=100, blank=True, null=True)
    class_id = models.CharField(max_length=100, blank=True, null=True)
    balance = models.CharField(max_length=100, blank=True, null=True)
    employees_id_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_schoolstaff'

class JkitepContactdetails(models.Model):
    db = 'test'
    contactid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='contactid', primary_key=True)
    contact_no = models.CharField(max_length=100)
    accountid = models.IntegerField(blank=True, null=True)
    salutation = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=80)
    firstname = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    reportsto = models.CharField(max_length=30, blank=True, null=True)
    training = models.CharField(max_length=50, blank=True, null=True)
    usertype = models.CharField(max_length=50, blank=True, null=True)
    contacttype = models.CharField(max_length=50, blank=True, null=True)
    otheremail = models.CharField(max_length=100, blank=True, null=True)
    secondaryemail = models.CharField(max_length=100, blank=True, null=True)
    donotcall = models.CharField(max_length=3, blank=True, null=True)
    emailoptout = models.CharField(max_length=3, blank=True, null=True)
    imagename = models.CharField(max_length=150, blank=True, null=True)
    reference = models.CharField(max_length=3, blank=True, null=True)
    notify_owner = models.CharField(max_length=3, blank=True, null=True)
    splastsms = models.DateTimeField(blank=True, null=True)
    isconvertedfromlead = models.CharField(max_length=3, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    pin_con = models.CharField(max_length=100, blank=True, null=True)
    class_id = models.CharField(max_length=100, blank=True, null=True)
    school_id = models.CharField(max_length=100, blank=True, null=True)
    balance = models.DecimalField(max_digits=27, decimal_places=8, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    benefit = models.CharField(max_length=100, blank=True, null=True)
    startbalance = models.CharField(max_length=100, blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    school_class_id = models.CharField(max_length=100, blank=True, null=True)
    balance_sum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_contactdetails'


class JkitepCrmentity(models.Model):
    db = 'test'
    crmid = models.IntegerField(primary_key=True)
    smcreatorid = models.IntegerField()
    smownerid = models.IntegerField()
    modifiedby = models.IntegerField()
    setype = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdtime = models.DateTimeField()
    modifiedtime = models.DateTimeField()
    viewedtime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    version = models.IntegerField()
    presence = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    smgroupid = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_crmentity'

class JkitepAccount(models.Model):
    db = 'test'
    accountid = models.OneToOneField('JkitepCrmentity', models.DO_NOTHING, db_column='accountid', primary_key=True)
    account_no = models.CharField(max_length=100)
    accountname = models.CharField(max_length=100)
    parentid = models.IntegerField(blank=True, null=True)
    account_type = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    annualrevenue = models.DecimalField(max_digits=25, decimal_places=8, blank=True, null=True)
    rating = models.CharField(max_length=200, blank=True, null=True)
    ownership = models.CharField(max_length=50, blank=True, null=True)
    siccode = models.CharField(max_length=50, blank=True, null=True)
    tickersymbol = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    otherphone = models.CharField(max_length=30, blank=True, null=True)
    email1 = models.CharField(max_length=100, blank=True, null=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    employees = models.IntegerField(blank=True, null=True)
    emailoptout = models.CharField(max_length=3, blank=True, null=True)
    notify_owner = models.CharField(max_length=3, blank=True, null=True)
    inn = models.CharField(max_length=30, blank=True, null=True)
    kpp = models.CharField(max_length=30, blank=True, null=True)
    splastsms = models.DateTimeField(blank=True, null=True)
    one_s_id = models.CharField(max_length=255, blank=True, null=True)
    isconvertedfromlead = models.CharField(max_length=3, blank=True, null=True)
    tags = models.CharField(max_length=1, blank=True, null=True)
    full_name_2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_account'

class JkitepModtrackerBasic(models.Model):
    db = 'test'
    id = models.IntegerField(primary_key=True)
    crmid = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    whodid = models.IntegerField(blank=True, null=True)
    changedon = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jkitep_modtracker_basic'


class LastChangeInJkitepModtrackerBasic(models.Model):
    db = 'default'
    id = models.IntegerField(primary_key=True)
    class Meta:
       verbose_name_plural = "ID Последнего изменения"

#@receiver(post_save, sender=Subject)
#def subject_obj_add(sender, instance, created, **kwargs):
 #   if created:
  #      creations_logger.info(f'Учитель \"{instance.teacherID.teacherName}\" добавил УРОК \"{instance.subjectName}\" классу \"{instance.cohortID.class_name}\".')

#@receiver(post_save, sender=Timetable)
#def time_tbl_obj_add(sender, instance, created, **kwargs):
 #   if created:
  #      creations_logger.info(f'Учитель \"{instance.subjectID.teacherID.teacherName}\" добавил в РАСПИСАНИЕ урок \"{instance.subjectID.subjectName}\" на \"{instance.date}\" с \"{instance.startTime}\" до \"{instance.endTime}\" классу \"{instance.cohortID.class_name}\".')

#@receiver(post_save, sender=regularGrade)
#def regularGrades_obj_add(sender, instance, created, **kwargs):
 #   if created:
  #      creations_logger.info(f'Учитель \"{instance.subjectID.teacherID.teacherName}\" поставил ОЦЕНКУ \"{instance.mark}\" за \"{instance.type}\" ученику \"{instance.studentID.studentName}\" за урок \"{instance.lesson.subjectID.subjectName}\".')

#@receiver(post_save, sender=finalGrade)
#def finalGrade_obj_add(sender, instance, created, **kwargs):
#    if created:
#        creations_logger.info(f'Учитель \"{instance.subjectID.teacherID.teacherName}\" поставил ГОДОВУЮ-ОЦЕНКУ \"{instance.mark}\" за \"{instance.type}\" ученику \"{instance.studentID.studentName}\" за урок \"{instance.subjectID.subjectName}\".')



# Signals that detect and log changes in forms.
#@receiver(pre_save, sender=Cohort)
#def teacher_obj_update(sender, instance, **kwargs):
#    if not instance._state.adding:
#        unchanged = Cohort.objects.get(pk=instance.pk)
#        updates_logger.info(f"Школа \"{instance.mainTeacherID.schoolID}\" изменила учителя \"{unchanged.mainTeacherID}\" на учителя \"{instance.mainTeacherID}\" у класса \"{instance.class_name}\".")

#@receiver(pre_save, sender=Subject)
#def subject_obj_update(sender, instance, **kwargs):
#    if not instance._state.adding:
#        unchanged = Subject.objects.get(pk=instance.pk)
#        updates_logger.info(f"Учитель \"{instance.teacherID.teacherName}\" изменил УРОК \"{instance.cohortID.class_name}\" класса с \"{unchanged.subjectName}\" на \'{instance.subjectName}\'.")

#@receiver(pre_save, sender=Timetable)
#def time_tbl_obj_update(sender, instance, **kwargs):
#    if not instance._state.adding:

#        unchanged = Timetable.objects.get(pk=instance.pk)

#        if unchanged.teacher != instance.teacher and unchanged.subjectID.subjectName == instance.subjectID.subjectName:
#            updates_logger.info(f"Учитель по \"{instance.subjectID.subjectName}\" \"{instance.subjectID.cohortID.class_name}\" класса на \"{instance.date}\" с \"{instance.startTime}\" до \"{instance.endTime}\" был изменён с \"{unchanged.teacher}\" на \"{instance.teacher}\".")

#        if unchanged.teacher != instance.teacher and unchanged.subjectID.subjectName != instance.subjectID.subjectName:
#            updates_logger.info(f"Учитель для \"{instance.subjectID.subjectName}\" был изменён с \"{unchanged.teacher}\" на \"{instance.teacher}\", РАСПИСАНИЕ \"{instance.subjectID.cohortID.class_name}\" класса было измененно с \"{unchanged.subjectID.subjectName}\" на \'{instance.subjectID.subjectName}\'.")

#        else:
#            updates_logger.info(f"Учитель \"{instance.subjectID.teacherID.teacherName}\" изменил РАСПИСАНИЕ класса \"{instance.subjectID.cohortID.class_name}\" с \"{unchanged.subjectID.subjectName}\" на \'{instance.subjectID.subjectName}\'.")


#@receiver(pre_save, sender=regularGrade)
def regularGrades_obj_update(sender, instance, **kwargs):
    if not instance._state.adding:
        unchanged = regularGrade.objects.get(pk=instance.pk)
        updates_logger.info(f"Учитель \"{instance.subjectID.teacherID.teacherName}\" изменил ОБЫЧНУЮ-оценку урока \"{instance.lesson.subjectID.subjectName}\" ученика \"{instance.studentID}\" c \"{unchanged.mark}\" на \'{instance.mark}\'.")

#@receiver(pre_save, sender=finalGrade)
def finalGrades_tbl_obj_update(sender, instance, **kwargs):
    if not instance._state.adding:
        unchanged = finalGrade.objects.get(pk=instance.pk)
        updates_logger.info(f"Учитель \"{instance.subjectID.teacherID.teacherName}\" изменил ИТОГОВУЮ-оценку урока \"{instance.lesson.subjectID.subjectName}\" ученика \"{instance.studentID}\" c \"{unchanged.mark}\" на \'{instance.mark}\'.")



#@receiver(pre_delete, sender=Subject)
def subject_obj_remove(sender, instance, **kwargs):
    deletions_logger.info(f"Учитель \"{instance.teacherID.teacherName}\" удалил УРОК \"{instance.subjectName}\" у \"{instance.cohortID.class_name}\" класса.")

#@receiver(pre_delete, sender=Timetable)
def time_tbl_obj_remove(sender, instance, **kwargs):
    deletions_logger.info(f'Учитель \"{instance.subjectID.teacherID.teacherName}\" удалил с РАСПИСАНИЯ урок \"{instance.subjectID.subjectName}\" на \"{instance.date}\" с \"{instance.startTime}\" до \"{instance.endTime}\" у \"{instance.cohortID.class_name}\" класса.')

#@receiver(pre_delete, sender=regularGrade)
def regularGrades_obj_remove(sender, instance, **kwargs):
    deletions_logger.info(f'Учитель \"{instance.subjectID.teacherID.teacherName}\" удалил ОЦЕНКУ \"{instance.mark}\" за \"{instance.type}\" ученика \"{instance.studentID.studentName}\"')

#@receiver(pre_delete, sender=finalGrade)
def finalGrades_obj_remove(sender, instance, **kwargs):
    deletions_logger.info(f'Учитель \"{instance.subjectID.teacherID.teacherName}\" удалил ГОДОВУЮ-ОЦЕНКУ \"{instance.mark}\" за \"{instance.type}\" ученика \"{instance.studentID.studentName}\".')
