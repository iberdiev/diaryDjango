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
#     print(a.text)
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

# URL = "http://127.0.0.1:8080/api/v1/get_cohorts/"
# cohorts = models.JkitepSchoolclasses.objects.raw("SELECT * FROM `jkitep_schoolclasses` INNER JOIN jkitep_crmentity on jkitep_schoolclasses.schoolclassesid = jkitep_crmentity.crmid and jkitep_crmentity.deleted = '0' and school_id IS NOT NULL")
# for cohort in cohorts:
#     class_name = cohort.label
#     schoolID = str(cohort.school_id) + "school"
#     teacherID = str(cohort.smownerid) + "teacher"
#     school_creator = models.CustomUser.objects.get(username=schoolID)
#     if not models.CustomUser.objects.filter(username=teacherID).exists():
#         continue
#     mainTeacherID = models.CustomUser.objects.get(username=teacherID).mainTeacher.pk
#     data = {"class_name": class_name,
#             "mainTeacherID": mainTeacherID,
#             "schoolID": schoolID,
#             "jkitepClassID": cohort.schoolclassesid}
#     a = requests.post(url = URL, data = data)
#     print(a.text)

#############################
# Getting and saving all students + attaching to parents and cohorts

# URL = "http://127.0.0.1:8080/api/v1/students/"
# students = models.JkitepContactdetails.objects.raw("SELECT * FROM `jkitep_contactdetails` INNER JOIN jkitep_crmentity on jkitep_contactdetails.accountid = jkitep_crmentity.crmid and jkitep_crmentity.deleted = '0' and school_class_id IS NOT NULL")
# for student in students:
#     print(student.school_class_id)
#     name = "{} {}".format(student.lastname, student.firstname)
#     if not models.Cohort.objects.filter(jkitepClassID=student.school_class_id).exists():
#         continue
#     cohortID = models.Cohort.objects.get(jkitepClassID=student.school_class_id).pk
#     parentID = models.CustomUser.objects.get(username=str(student.accountid)+"parent")
#     data = {"studentName": name,"cohort": cohortID,"parent": parentID}
#     a = requests.post(url = URL, data = data)
#     print(a.text)

#############################
# Script that checks all the changes in JkitepDB and applies them in djangoDB

lastChangeID = str(models.LastChangeInJkitepModtrackerBasic.objects.last().id)
print("######### Django Last Change ID: " + lastChangeID)
# SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = 443177
changes = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` WHERE id > "+ lastChangeID)

for change in changes:
    changeID = str(change.id)
    if change.module == "Schools":
        if change.status == 2:
            pass # Done
            # specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
            # print(change.id, "- School has been created")
            # username = str(specificChanges[0].crmid) + "school"
            # for specificChange in specificChanges:
            #     if specificChange.fieldname == "label":
            #         schoolName = specificChange.postvalue
            # data = {"name": schoolName,
            #         "username":username,
            #         "user_role": 1,
            #         "password1":username,
            #         "password2":username}
            # a = requests.post(url = "http://127.0.0.1:8080/api/v1/registration/", data = data)
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.status == 0:
            continue
            print(change.id, "- School has been altered")
            specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
            for specificChange in specificChanges:
                if specificChange.fieldname == "label":
                    changedName = specificChange.postvalue
                    print(changedName)
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.status == 1:
            continue
            specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` WHERE id = " + changeID)
            print(change.id, "- School has been deleted")
            deletedSchool = specificChanges[0].crmid
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
    elif change.module == "SchoolStaff":
        continue
        if change.status == 2:
            specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
            for specificChange in specificChanges:
                if specificChange.fieldname == "label":
                    name = specificChange.postvalue
                if specificChange.fieldname == "employees_id_user":
                    username = str(specificChange.postvalue) + "teacher"
                if specificChange.fieldname == "school_id":
                    schoolUsername = str(specificChange.postvalue) + "school"
            data = {"username": username,
                    "name": name,
                    "user_role": 2,
                    "password1":username,
                    "password2":username}
            a = requests.post(url = "http://127.0.0.1:8080/api/v1/registration/", data = data)
            schoolID = models.CustomUser.objects.get(username=schoolUsername)
            teacherID = models.CustomUser.objects.get(username=username)
            models.Teacher.objects.create(teacherName=name, schoolID=schoolID, teacherID=teacherID)
            print(change.id, "- Staff has been created")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.status == 0:
            pass
            # print(change.id, "- Staff has been altered")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.status == 1:
            pass
            # print(change.id, "- Staff has been deleted")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
    elif change.module == "SchoolClasses":
        continue
        if change.status == 2:
            specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
            for specificChange in specificChanges:
                if specificChange.fieldname == "label":
                    className = specificChange.postvalue
                if specificChange.fieldname == "school_id":
                    schoolUsername = str(specificChange.postvalue) + "school"
                if specificChange.fieldname == "record_id":
                    jkitepClassID = specificChange.postvalue
                if specificChange.fieldname == "assigned_user_id":
                    teacherUsername = str(specificChange.postvalue) + "teacher"
            schoolID = models.CustomUser.objects.get(username=schoolUsername)
            mainTeacherID = models.CustomUser.objects.get(username=teacherUsername).mainTeacher.pk
            data = {"class_name": className,
                    "mainTeacherID": mainTeacherID,
                    "schoolID": schoolID,
                    "jkitepClassID": jkitepClassID}
            a = requests.post(url = "http://127.0.0.1:8080/api/v1/get_cohorts/", data = data)
            print(change.id, "- Cohort has been created")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.status == 0:
            pass
            # print(change.id, "- Cohort has been altered")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.status == 1:
            pass
            # print(change.id, "- Cohort has been deleted")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
    elif change.module == "Contacts":
        if change.status == 2:
            specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
            for specificChange in specificChanges:
                if specificChange.fieldname == "label":
                    studentName = specificChange.postvalue
                if specificChange.fieldname == "school_class_id":
                    jkitepClassID = specificChange.postvalue
                if specificChange.fieldname == "account_id":
                    parentUsername = str(specificChange.postvalue) + "parent"
            cohortID = models.Cohort.objects.get(jkitepClassID=jkitepClassID).pk
            if models.CustomUser.objects.filter(username=parentUsername).exists():
                parentID = models.CustomUser.objects.get(username=parentUsername)
                data = {"studentName": studentName,"cohort": cohortID,"parent": parentID}
                a = requests.post(url = "http://127.0.0.1:8080/api/v1/students/", data = data)
            else:
                data = {"studentName": studentName,"cohort": cohortID, "parent": ""}
                a = requests.post(url = "http://127.0.0.1:8080/api/v1/students/", data = data)
            print(change.id, "- Student has been created")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)

        elif change.status == 0:
            pass
            # print(change.id, "- Student has been altered")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.status == 1:
            pass
            # print(change.id, "- Student has been deleted")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
    elif change.module == "Accounts":
        if change.status == 2:
            continue
            specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
            parentUsername = str(specificChanges[0].crmid) + "parent"
            for specificChange in specificChanges:
                if specificChange.fieldname == "label":
                    parentName = specificChange.postvalue
            data = {"username": parentUsername,
                    "name": str(parentName),
                    "user_role": 3,
                    "password1":parentUsername,
                    "password2":parentUsername}
            a = requests.post(url = "http://127.0.0.1:8080/api/v1/registration/", data = data)
            print(change.id, "- Parent has been created")
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.status == 0:
            pass
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            # print(change.id, "- Parent has been altered")
        elif change.status == 1:
            pass
            models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            # print(change.id, "- Parent has been deleted")

# При создании школы -> modtracker_basic "module = Schools" and "status = 2"
# При изменении школы -> modtracker_basic "module = Schools" and "status = 0"
# При удалении школы -> modtracker_basic "module = Schools" and "status = 1"
#
# При создании сотрудника школы "module = SchoolStaff" and "status = 2"
# При изменении сотрудника школы "module = SchoolStaff" and "status = 0"
# При удалении сотрудника школы "module = SchoolStaff" and "status = 1"
#
# При создании класса  "module = SchoolClasses" and "status = 2"
# При изменении класса "module = SchoolClasses" and "status = 0"
# При удалении класса "module = SchoolClasses" and "status = 1"
#
# При создании ученика "module = Contacts" and "status = 2"
# При изменении ученика "module = Contacts" and "status = 0"
# При удалении ученика "module = Contacts" and "status = 1"
#
# При создании родителя "module = Accounts" and "status = 2"
# При изменении родителя "module = Accounts" and "status = 0"
# При удалении родителя "module = Accounts" and "status = 1"

#############################
