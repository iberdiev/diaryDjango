from celery import shared_task
from celery.decorators import task
from django.core.mail import send_mail
import datetime, requests
from . import models

#@shared_task
#def sendEmailToSetPassword(email, code):
#    send_mail('Hello from Iskender.', str(code), 'onlinediaryputinbyte@yandex.ru', [email], fail_silently=False)

@shared_task
def sendEmailToSetPassword():
    send_mail('Hello from Iskender.', str(4567890), 'onlinediaryputinbyte@yandex.ru', ['iskender.berdiev@gmail.com'], fail_silently=False)




# @shared_task
# def periodicPrintHelloWorld():
#     print("Hello World")

@shared_task
def duplicateTodaysLessonsToNextWeek():
    today = datetime.date.today()
    oneWeekLater = today + datetime.timedelta(days=7)
    todaysLessons = models.Timetable.objects.filter(date=today)

    for lesson in todaysLessons:
        futureLesson = models.Timetable.objects.filter(date=oneWeekLater, startTime=lesson.startTime, cohortID=lesson.cohortID)
        if len(futureLesson) == 0:
            lessonToCreate = lesson
            lessonToCreate.date, lessonToCreate.pk, lessonToCreate.homework = oneWeekLater, None, ''
            lessonToCreate.save()

@shared_task
def synchronizationWithJKitepDB():
    lastChangeID = str(models.LastChangeInJkitepModtrackerBasic.objects.last().id)
    print(lastChangeID)
    changes = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` WHERE id > "+ lastChangeID)
    print(len(changes))
    for change in changes:
        changeID = str(change.id)
        if change.module == "Schools":
            if change.status == 2:
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
                print(change.id, "- School has been created")
                username = str(specificChanges[0].crmid) + "school"
                for specificChange in specificChanges:
                    if specificChange.fieldname == "label":
                        schoolName = specificChange.postvalue
                data = {"name": schoolName,
                        "username":username,
                        "user_role": 1,
                        "password1":username,
                        "password2":username}
                a = requests.post(url = "http://diary.putinbyte.com:8000/api/v1/registration/", data = data)
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 0:
                print(change.id, "- School has been altered")
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
                schoolUsername = str(specificChanges[0].crmid) + "school"
                for specificChange in specificChanges:
                    if specificChange.fieldname == "label":
                        changedName = specificChange.postvalue
                        break
                school = models.CustomUser.objects.get(username=schoolUsername)
                school.name=changedName
                school.save()
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 1:
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` WHERE id = " + changeID)
                print(change.id, "- School has been deleted")
                models.CustomUser.objects.get(username=(str(specificChanges[0].crmid)+"school")).delete()
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.module == "SchoolStaff":
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
                a = requests.post(url = "http://diary.putinbyte.com:8000/api/v1/registration/", data = data)
                schoolID = models.CustomUser.objects.get(username=schoolUsername)
                teacherID = models.CustomUser.objects.get(username=username)
                if not models.CustomUser.objects.filter(username=teacherID).exists():
                    models.Teacher.objects.create(teacherName=name, schoolID=schoolID, teacherID=teacherID)
                print(change.id, "- Staff has been created")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 0:
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = {} INNER JOIN jkitep_crmentity on jkitep_modtracker_basic.crmid = jkitep_crmentity.crmid".format(changeID))
                teacher = models.CustomUser.objects.get(username=str(specificChanges[0].smownerid)+"teacher")
                for specificChange in specificChanges:
                    if specificChange.fieldname == "label":
                        teacher.name = specificChange.postvalue
                        teacher.save()
                        teacher = teacher.mainTeacher
                        teacher.teacherName = specificChange.postvalue
                        teacher.save()
                    if specificChange.fieldname == "school_id":
                        school = models.CustomUser.objects.get(username=str(specificChange.postvalue)+"school")
                        teacher = models.CustomUser.objects.get(username=str(specificChange.smownerid)+"teacher").mainTeacher
                        teacher.schoolID = school
                        teacher.save()
                print(change.id, "- Staff has been altered")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 1:
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_crmentity on jkitep_modtracker_basic.crmid = jkitep_crmentity.crmid and jkitep_modtracker_basic.id = " + changeID)
                teacher = models.CustomUser.objects.get(username=str(specificChanges[0].smownerid)+"teacher").delete()
                print(change.id, "- Staff has been deleted")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.module == "SchoolClasses":
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
                a = requests.post(url = "http://diary.putinbyte.com:8000/api/v1/get_cohorts/", data = data)
                print(change.id, "- Cohort has been created")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 0:
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
                for specificChange in specificChanges:
                    if specificChange.fieldname == "label":
                        cohort = models.Cohort.objects.get(jkitepClassID=specificChange.crmid)
                        cohort.class_name = specificChange.postvalue
                        cohort.save()
                    if specificChange.fieldname == "school_id":
                        cohort = models.Cohort.objects.get(jkitepClassID=specificChange.crmid)
                        cohort.school_creator = models.CustomUser.objects.get(username=str(specificChange.postvalue)+"school")
                        cohort.save()
                    if specificChange.fieldname == "assigned_user_id":
                        cohort = models.Cohort.objects.get(jkitepClassID=specificChange.crmid)
                        cohort.mainTeacherID = models.CustomUser.objects.get(username=str(specificChange.postvalue)+"teacher").mainTeacher
                        cohort.save()
                print(change.id, "- Cohort has been altered")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 1:
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` WHERE id = " + changeID)
                models.Cohort.objects.get(jkitepClassID=specificChanges[0].crmid).delete()
                print(change.id, "- Cohort has been deleted")
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
                    a = requests.post(url = "http://diary.putinbyte.com:8000/api/v1/students/", data = data)
                else:
                    data = {"studentName": studentName,"cohort": cohortID, "parent": ""}
                    a = requests.post(url = "http://diary.putinbyte.com:8000/api/v1/students/", data = data)
                print(change.id, "- Student has been created")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 0:
                continue
                # specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
                # for specificChange in specificChanges:
                #     if specificChange.fieldname == "label":
                #         print(specificChange.prevalue)
                #         studentPreviousName = specificChange.prevalue
                #         studentName = specificChange.postvalue
                #     if specificChange.fieldname == "school_class_id":
                #         previousCohort = specificChange.prevalue
                #         currentCohort = specificChange.postvalue
                #     if specificChange.fieldname == "assigned_user_id":
                #         previousTeacher = specificChange.prevalue
                #         currentTeacher = specificChange.postvalue
                # student = models.Student.objects.get(studentName=studentPreviousName)
                # print(student.studentName)
                # print(change.id, "- Student has been altered")
                # models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 1:
                continue
                # print(change.id, "- Student has been deleted")
                # models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
        elif change.module == "Accounts":
            if change.status == 2:
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
                a = requests.post(url = "http://diary.putinbyte.com:8000/api/v1/registration/", data = data)
                print(change.id, "- Parent has been created")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 0:
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` INNER JOIN jkitep_modtracker_detail on jkitep_modtracker_detail.id = jkitep_modtracker_basic.id and jkitep_modtracker_basic.id = " + changeID)
                for specificChange in specificChanges:
                    if specificChange.fieldname == "label":
                        parent = models.CustomUser.objects.get(username=str(specificChange.crmid)+"parent")
                        parent.name = specificChange.postvalue
                        parent.save()
                print(change.id, "- Parent has been altered")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
            elif change.status == 1:
                specificChanges = models.JkitepModtrackerBasic.objects.raw("SELECT * FROM `jkitep_modtracker_basic` WHERE id = " + changeID)
                models.CustomUser.objects.get(username=str(specificChanges[0].crmid)+"parent").delete()
                print(change.id, "- Parent has been deleted")
                models.LastChangeInJkitepModtrackerBasic.objects.create(id=change.id)
    return print("Done synchronization with JKitep DB")

