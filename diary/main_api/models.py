from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CustomUser(AbstractUser):
    db = 'default'
    name = models.CharField(blank=True, max_length=255)
    password = models.CharField(max_length=100)
    user_role = models.IntegerField()
    def __str__(self):
        return self.username

class Cohort(models.Model):
    db = 'default'
    school_creator = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='cohorts')
    mainTeacherID = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='mainCohorts')
    class_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    db = 'default'
    studentName = models.CharField(max_length = 100)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.studentName


class Teacher(models.Model):
    db = 'default'
    teacherName = models.CharField(max_length = 100)
    schoolID = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teachers')
    teacherID = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name='mainTeacher')

    def __str__(self):
        return self.teacherName

class Subject(models.Model):
    db = 'default'
    subjectName = models.CharField(max_length = 100)
    cohortID = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='subjects')
    teacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects', null=True)
    def __str__(self):
        return self.subjectName

class regularGrade(models.Model):
    db = 'default'
    subjectID = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='regularGrades')
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='regularGrades')
    pub_date = models.DateTimeField('date_published', auto_now_add = True)
    mark = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(2)])
    COMMENT_CHOICES = (
        (1, 'Контрольная работа'),
        (2, 'Классная работа'),
        (3, 'Устный зачёт'),
        (4, 'Домашняя работа'),
        (5, 'Неизвестно'),
    )
    comment = models.PositiveSmallIntegerField(choices=COMMENT_CHOICES, default=5)

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
    omsu = models.CharField(max_length=100, blank=True, null=True)
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
