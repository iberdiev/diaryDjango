from . import models, serializers, tasks
# from django.db import models
from rest_framework import generics, status, viewsets
from main_api.models import CustomUser
from main_api.serializers import UserSerializer
from rest_auth.views import LoginView, APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.utils.timezone import datetime
import random, requests



class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    def perform_create(self, serializer):
        user_role = int(self.request.data["user_role"])
        if user_role == 1:
            serializer.save()
            username = self.request.data["username"]
            user = models.CustomUser.objects.get(username=username)
            user.set_password(username)
            user.save()
        elif user_role == 2:
            username = self.request.data["username"]
            serializer.save()
            user = models.CustomUser.objects.get(username=self.request.data["username"])
            user.set_password(username)
            user.save()
            schoolID = self.request.user
            models.Teacher.objects.create(teacherName=self.request.data["name"], schoolID=schoolID, teacherID=user)
        elif user_role == 3:
            serializer.save()
            username = self.request.data["username"]
            user = models.CustomUser.objects.get(username=username)
            user.set_password(username)
            user.save()

@permission_classes((IsAuthenticated, ))
class ChangeTeacherOfSubject(APIView):
    def post(self,request, format=None):
        subjectToChange = request.data['subject']
        teacherToChange = request.data['teacher']
        subject = models.Subject.objects.get(pk=subjectToChange)
        subject.teacherID = models.Teacher.objects.get(pk=teacherToChange)
        subject.save()
        return Response("Done")

@permission_classes((IsAuthenticated, ))
class getTheChild(APIView):
    def get(self,request, format=None):
        # studentID = models.CustomUser.objects.get(pk=self.request.user).name
        child = models.CustomUser.objects.get(pk=self.request.user.pk).child
        data = serializers.StudentSerializer(child, many=True).data
        return Response(data)


# @permission_classes((IsAuthenticated, ))
class SubjectsListView(APIView):
    def get(self,request):
        cohort = self.request.query_params.get('cohortID')
        subjects = models.Cohort.objects.get(pk=cohort).subjects
        data = serializers.SubjectSerializer(subjects, many=True).data
        return Response(data)
    def post(self, request, format=None):
        serializer = serializers.SubjectSerializer(data=request.data)
        if serializer.is_valid():
            cohortID = models.Cohort.objects.get(pk=request.data["cohortID"])
            teacherID = models.Teacher.objects.get(pk=request.data["teacherID"])
            serializer.save(cohortID=cohortID,teacherID=teacherID)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, format=None):
        subject = models.Subject.objects.get(pk=request.data["pk"])
        teacherID = models.Teacher.objects.get(pk=request.data["teacherID"])
        serializer = serializers.SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save(teacherID=teacherID)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        subject = models.Subject.objects.get(pk=request.query_params.get('pk'))
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes((IsAuthenticated, ))
class TeachersListView(APIView):
    def get(self, request):
        teachers = request.user.teachers
        data = serializers.TeacherSerializer(teachers, many=True).data
        return Response(data)
    def post(self, request, format=None):
        serializer = serializers.TeacherSerializer(data=request.data)
        teacherName = request.data['teacherName']
        schoolID = models.CustomUser.objects.get(username=request.data['schoolID'])
        if serializer.is_valid():
            serializer.save(schoolID=schoolID)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_auth.registration.views import RegisterView

class CustomRegisterView(RegisterView):
    queryset = CustomUser.objects.all()

# @permission_classes((IsAuthenticated, ))
class StudentsListView(APIView):
    def get(self, request):
        cohort = self.request.query_params.get('cohort')
        students = models.Cohort.objects.get(pk=cohort).students
        data = serializers.StudentSerializer(students, many=True).data
        return Response(data)

    def post(self, request, format=None):

        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            if self.request.data["parent"]:
                serializer.save(cohort=models.Cohort.objects.get(pk=request.data['cohort']),
                                parent=models.CustomUser.objects.get(username=request.data['parent']))
            else:
                serializer.save(cohort=models.Cohort.objects.get(pk=request.data['cohort']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @permission_classes((IsAuthenticated, ))
class CohortsView(APIView):
    def get(self, request):
        # token = Token.objects.get(key=response.data['token'])
        # my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        # user_id = Token.objects.get(key=my_token).user_id
        cohorts = models.Cohort.objects.filter(school_creator=request.user)
        data = serializers.CohortSerializer(cohorts, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = serializers.CohortSerializer(data=request.data)
        if serializer.is_valid():
            school = CustomUser.objects.get(username=request.data["schoolID"])
            teacher = models.Teacher.objects.get(pk=request.data["mainTeacherID"])
            serializer.save(school_creator=school, mainTeacherID=teacher, jkitepClassID=request.data["jkitepClassID"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_role': user.user_role,
            'name': user.name,
        })

@permission_classes((IsAuthenticated, ))
class MainCohortList(APIView):
    def get(self, request):
        # my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        # user_id = Token.objects.get(key=my_token).user_id
        # username = CustomUser.objects.get(pk=user_id).username
        cohorts = models.CustomUser.objects.get(username=request.user.username).mainCohorts
        data = serializers.CohortSerializer(cohorts, many=True).data
        return Response(data)


@permission_classes((IsAuthenticated, ))
class givenSubjectsOfTeacher(APIView):
    def get(self, request):
        # my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        # user_id = Token.objects.get(key=my_token).user_id
        # username = CustomUser.objects.get(pk=user_id).username
        subjects = models.CustomUser.objects.get(username=request.user.username).mainTeacher.subjects
        data = serializers.SubjectCohortSerializer(subjects, many=True).data
        return Response(data)

@permission_classes((IsAuthenticated, ))
class getUniqueCohortsByTaught(APIView):
    def get(self, request):
        # my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        # user_id = Token.objects.get(key=my_token).user_id
        # username = CustomUser.objects.get(pk=user_id).username
        subjects = models.CustomUser.objects.get(username=request.user.username).mainTeacher.subjects
        data = serializers.UniqueCohortsBySubjectsForTeacher(subjects, many=True).data
        mainCohorts = request.user.mainTeacher.mainCohorts
        notTaughtCohorts = serializers.CohortSerializerOnlyNameAndID(mainCohorts, many=True).data
        return Response(data + notTaughtCohorts)
# @permission_classes((IsAuthenticated, ))
# class CohortsRelatedToTeacher(APIView):
#     def get(self, request):
#         # my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
#         # user_id = Token.objects.get(key=my_token).user_id
#         # username = CustomUser.objects.get(pk=user_id).username
#         subjects = models.Teacher.objects.get(teacherID=request.user).subjects
#         print(subjects)
#         # subjects = models.CustomUser.objects.get(username=request.user.username).mainTeacher.subjects
#         data = serializers.SubjectCohortSerializer(subjects, many=True).data
#         return Response(data)

@permission_classes((IsAuthenticated, ))
class GivenSubjectStudentListView(APIView):
    def get(self, request):
        subject = self.request.query_params.get('subject')
        cohort = models.Subject.objects.get(pk=subject).cohortID.pk
        students = models.Cohort.objects.get(pk=cohort).students
        data = serializers.StudentSerializer(students, many=True).data
        return Response(data)

# @permission_classes((IsAuthenticated, ))
class RegularGradesListView(APIView):
    def get(self, request):
        date = self.request.query_params.get('date')
        student = self.request.query_params.get('studentID')
        grades = models.regularGrade.objects.filter(studentID = student)
        data = serializers.RegularGradeSerializer(grades, many=True).data
        return Response(data)
# http://127.0.0.1:8080/api/v1/regularGrades/?date=2020-01-12&studentID=22

    def post(self, request, format=None):
        serializer = serializers.RegularGradeSerializer(data=request.data)
        if serializer.is_valid():
            student = models.Student.objects.get(pk=request.data["studentID"])
            teacherID = request.user.mainTeacher
            serializer.save(studentID=student, teacherID=teacherID)
            return Response("OK")
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, format=None):
        regularGrade = models.regularGrade.objects.get(pk=(request.data["pk"]))
        serializer = serializers.ChangeRegularGradeSerializer(regularGrade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        regularGrade = models.regularGrade.objects.get(pk=request.query_params.get('pk'))
        regularGrade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##### asldjfklasdjfklasdjlfkjasd;lfjkl
class CohortRegularGradesOneSubjectView(APIView):
    def get(self, request):
        cohortID = self.request.query_params.get('cohortID')
        student = models.Cohort.objects.get(pk=cohortID).students
        subjectID = self.request.query_params.get('subjectID')
        gradeType = self.request.query_params.get('type')
        data = serializers.StudentGradesOneSubjectSerializer(student, many=True, context={"subjectID": subjectID, "type":gradeType}).data
        timetable = models.Timetable.objects.filter(subjectID=subjectID, date__day__lte=datetime.today().day)
        timetables = serializers.TimetableSerializer(timetable, many=True).data
        return Response({"grades": data, "timetables": timetables})
        # filter(studentID=student,lesson__subjectID=self.context["subjectID"],type=6, lesson__date__day__lte=today)
    # def post(self, request, format=None):
    #     serializer = serializers.RegularGradeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentSubjectFinalGradesView(APIView):
    def get(self, request):
        studentID = self.request.query_params.get('studentID')
        subjectID = self.request.query_params.get('subjectID')
        grades = models.finalGrade.objects.filter(subjectID = subjectID, studentID = studentID)
        data = serializers.FinalGradeSerializer(grades, many=True).data
        return Response(data)

class CohortSubjectFinalGradesView(APIView):
    def get(self, request):
        cohortID = self.request.query_params.get('cohortID')
        subjectID = self.request.query_params.get('subjectID')
        students = models.Cohort.objects.get(pk=cohortID).students
        data = serializers.StudentFinalGradesSerializer(students, many=True).data
        return Response(data)
    def post(self, request, format=None):
        serializer = serializers.FinalGradeSerializer(data=request.data)
        if serializer.is_valid():
            # student = models.Student.objects.get(pk=request.data["studentID"])
            # teacherID = request.user.mainTeacher
            serializer.save()
            return Response("OK")
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        finalGrade = models.finalGrade.objects.get(pk=(request.data["pk"]))
        serializer = serializers.ChangeFinalGradeSerializer(finalGrade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        finalGrade = models.finalGrade.objects.get(pk=request.query_params.get('pk'))
        finalGrade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes((IsAuthenticated, ))
class TimetableByCohortWithOneStudentsGradesView(APIView):
    def get(self, request):
        cohortID = self.request.query_params.get('cohortID')
        date = self.request.query_params.get("date")
        student = self.request.query_params.get('studentID')
        timetables = models.Timetable.objects.filter(cohortID=cohortID, date = date).order_by("startTime")
        data = serializers.TimetableWithOneStudentSerializer(timetables, many=True, context={"studentID": student}).data
        return Response(data)

class getStudentProfile(APIView):
    def get(self, request):
        studentID = self.request.query_params.get('studentID')
        student = models.Student.objects.get(pk=studentID)
        data = serializers.StudentProfileSerializer(student).data
        return Response(data)
        # return Response(data)

class TimetableByCohortView(APIView):
    def get(self, request):
        cohortID = self.request.query_params.get('cohortID')
        date = self.request.query_params.get("date")
        timetables = models.Timetable.objects.filter(cohortID=cohortID, date = date).order_by("startTime")
        data = serializers.TimetableSerializer(timetables, many=True).data
        return Response(data)

# http://127.0.0.1:8080/api/v1/timetableByCohort/?cohortID=3&date=2020-01-12
# curl -i -H "Accept: application/json" http://127.0.0.1:8080/api/v1/timetableByCohort/?cohortID=17

    def post(self, request, format=None):
        serializer = serializers.TimetableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# curl -d '{"teacher":2, "cohortID": 17, "subjectID": 22, "date" : "2020-01-09", "startTime": "15:40:00", "endTime": "15:45:00"}' -H "Content-Type: application/json" http://127.0.0.1:8080/api/v1/timetableByCohort/

    def put(self, request, format=None):
        timetable = models.Timetable.objects.get(pk=(request.data["pk"]))
        serializer = serializers.ChangeTimetableSerializer(timetable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        lesson = models.Timetable.objects.get(pk=request.query_params.get('pk'))
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TimetableByTeacherView(APIView):
    def get(self, request):
        teacherID = self.request.query_params.get('teacherID')
        date = self.request.query_params.get("date")
        teacher = models.Teacher.objects.get(pk=teacherID).timetable.order_by("startTime")
        # teacher = models.Teacher.objects.get(pk=teacherID).timetable.filter(date="2020-01-08")
        data = serializers.FilteredTimetableSerializer(teacher, many=True, context={"date": date}).data
        return Response(data)

class getTeacherID(APIView):
    def get(self, request):
        teacherID = models.CustomUser.objects.get(username=request.user.username).mainTeacher.pk
        return Response(teacherID)

class StudentIDSubjectsRegularFinalGradesView(APIView):
    def get(self, request):
        studentID = self.request.query_params.get('studentID')
        student = models.Student.objects.get(pk=studentID)
        subjects = models.Subject.objects.filter(cohortID=student.cohort)
        data = serializers.SubjectsRegularFinalGradesSerializer(subjects, many=True, context={"studentID": student.pk}).data
        return Response(data)

class SendResetCode(APIView):
    def get(self, request):
        user = models.CustomUser.objects.get(username=self.request.query_params.get('username'))
        code = random.randint(1000,9999)
        user.codeToResetPassword = code
        user.save()
        tasks.sendEmailToSetPassword.delay(user.email, code)
        return Response("На вашу почту отправим код для восстановления пароля в течении 1ой минуты!")

class SetPasswordView(APIView):
    def post(self, request):
        user = models.CustomUser.objects.get(username=request.data["username"])
        if user.codeToResetPassword == int(request.data["code"]):
            user.set_password(request.data["password"])
            user.save()
        else:
            return Response("Неверный код.")
        return Response("Пароль был изменен.")

class CallToNumber(APIView):
    def get(self, request):
        if self.request.query_params.get('username'):
            headers = {"X-AUTH-TOKEN": "UFzwQZMugSrMxCd7yW9PfNVX"}
            user = models.CustomUser.objects.get(username=self.request.query_params.get('username'))
            response = requests.get("http://192.168.0.89:3000/api/request/{}/".format(user.phoneNumber), headers=headers).json()
            user.codeToResetPassword = int(response['data']['gateway']['phone'])
            user.save()
            return Response("Звонок был совершен.")
        return Response("Неверно введен номер телефона.")
