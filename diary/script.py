import os, django, requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diary.settings")
django.setup()
from main_api import models


##############################
# Registering all availabe schools

# URL = "http://127.0.0.1:8080/api/v1/registration/"
# schools = models.JkitepSchools.objects.raw("SELECT * FROM `jkitep_schools` INNER JOIN jkitep_crmentity on jkitep_schools.schoolsid = jkitep_crmentity.crmid and jkitep_crmentity.deleted = 0" )
# for school in schools:
#
#     asdf = str(school.schoolsid)+"school"
#
#     data = {"name": school.label,
#            "username":asdf,
#            "user_role": 1,
#            "password1":asdf,
#            "password2":asdf}
    # a = requests.post(url = URL, data = data)

#############################
#Registering all availabe parents

# URL = "http://127.0.0.1:8080/api/v1/registration/"
# parents = models.JkitepAccount.objects.raw("SELECT * FROM `jkitep_account` INNER JOIN jkitep_crmentity on jkitep_account.accountid = jkitep_crmentity.crmid and jkitep_crmentity.deleted = '0'")


# for parent in parents:
#    name = parent.accountname
#    asdf = str(parent.accountid.crmid) + "parent"
#    data = {"username": asdf,
#            "name": str(name),
#            "user_role": 3,
#            "password1":asdf,
#            "password2":asdf}
#    a = requests.post(url = URL, data = data)

#############################
# Registering all teachers + adding Teacher models by connecting to Account.CustomUser + School.CustomUser

# URL = "http://127.0.0.1:8080/api/v1/registration/"
# teachers = models.JkitepSchoolstaff.objects.raw("SELECT * FROM `jkitep_schoolstaff` INNER JOIN jkitep_crmentity on jkitep_schoolstaff.schoolstaffid = jkitep_crmentity.crmid and jkitep_crmentity.deleted = '0'")
# for teacher in teachers:
#     username = str(teacher.employees_id_user) + "teacher"
#     if teacher.label:
#         name = teacher.label
#     else:
#         name = teacher.firstname + teacher.lastname
#     data = {"username": username,
#             "name": name,
#             "user_role": 2,
#             "password1":username,
#             "password2":username}
#     print(username)
#     a = requests.post(url = URL, data = data)
#     if teacher.school_id:
#         schoolID = models.CustomUser.objects.get(username=str(teacher.school_id) + "school")
#     else:
#         schoolID = None
#     teacherID = models.CustomUser.objects.get(username=str(teacher.employees_id_user) + "teacher")
#     models.Teacher.objects.create(teacherName=name, schoolID=schoolID, teacherID=teacherID)

#############################
# Setting all the passwords of all users to their username

# users = models.CustomUser.objects.all()
# for user in users:
#     print(user.pk)
#     user.set_password(user.username)
#     user.save()

#############################
# Getting and saving all cohorts + attaching them to schools.CustomerUser and teachers.Teacher
# JkitepSchoolclasses.objects.raw("SELECT * FROM `jkitep_schoolclasses` INNER JOIN jkitep_crmentity on jkitep_schoolclasses.schoolclassesid = jkitep_crmentity.crmid and jkitep_crmentity.deleted = '0' and school_id=7949")
# school_creator = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='cohorts')
# mainTeacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, related_name='mainCohorts')
# class_name = models.CharField(max_length = 100)
# URL = "http://127.0.0.1:8080/api/v1/get_cohorts/"
# cohorts = models.JkitepSchoolclasses.objects.raw("SELECT * FROM `jkitep_schoolclasses` INNER JOIN jkitep_crmentity on jkitep_schoolclasses.schoolclassesid = jkitep_crmentity.crmid and jkitep_crmentity.deleted = '0' and school_id IS NOT NULL")
# for cohort in cohorts:
#     class_name = cohort.label
#     schoolID = str(cohort.school_id) + "school"
#     teacherID = str(cohort.smownerid) + "teacher"
#     print(class_name)
#     print(schoolID)
#     print(teacherID)
#     school_creator = models.CustomUser.objects.get(username=schoolID)
#     if not models.CustomUser.objects.filter(username=teacherID).exists():
#         continue
#     mainTeacherID = models.CustomUser.objects.get(username=teacherID).mainTeacher.pk
#     data = {"class_name": class_name,
#             "mainTeacherID": mainTeacherID,
#             "schoolID": schoolID}
#     a = requests.post(url = URL, data = data)

#############################
# Getting all students
