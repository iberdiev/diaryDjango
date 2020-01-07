from . import models, serializers
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
class SubjectsListView(APIView):
    def get(self,request):
        cohort = self.request.query_params.get('cohort')
        subjects = models.Cohort.objects.get(pk=cohort).subjects
        data = serializers.SubjectSerializer(subjects, many=True).data
        return Response(data)
    def post(self, request, format=None):
        serializer = serializers.SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cohortID=models.Cohort.objects.get(pk=request.data['cohort']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated, ))
class TeachersListView(APIView):
    def get(self, request):
        school = self.request.query_params.get('school')
        teachers = models.CustomUser.objects.get(username=school).teachers
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



@permission_classes((IsAuthenticated, ))
class StudentsListView(APIView):
    def get(self, request):
        cohort = self.request.query_params.get('cohort')
        students = models.Cohort.objects.get(pk=cohort).students
        data = serializers.StudentSerializer(students, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cohort=models.Cohort.objects.get(pk=request.data['cohort']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated, ))
class CohortsView(APIView):
    def get(self, request):
        # token = Token.objects.get(key=response.data['token'])
        my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        user_id = Token.objects.get(key=my_token).user_id
        cohorts = models.Cohort.objects.filter(school_creator=user_id)
        data = serializers.CohortSerializer(cohorts, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = serializers.CohortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(school_creator=request.user)
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
            'user_role': user.user_role
        })

@permission_classes((IsAuthenticated, ))
class MainCohortList(APIView):
    def get(self, request):
        my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        user_id = Token.objects.get(key=my_token).user_id
        username = CustomUser.objects.get(pk=user_id).username
        cohorts = models.CustomUser.objects.get(username=username).mainCohorts
        data = serializers.CohortSerializer(cohorts, many=True).data
        return Response(data)


@permission_classes((IsAuthenticated, ))
class givenSubjectsOfTeacher(APIView):
    def get(self, request):
        my_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        user_id = Token.objects.get(key=my_token).user_id
        username = CustomUser.objects.get(pk=user_id).username
        subjects = models.CustomUser.objects.get(username=username).mainTeacher.subjects
        data = serializers.SubjectCohortSerializer(subjects, many=True).data
        return Response(data)

@permission_classes((IsAuthenticated, ))
class GivenSubjectStudentListView(APIView):
    def get(self, request):
        subject = self.request.query_params.get('subject')
        cohort = models.Subject.objects.get(pk=subject).cohortID.pk
        students = models.Cohort.objects.get(pk=cohort).students
        data = serializers.StudentSerializer(students, many=True).data
        return Response(data)

@permission_classes((IsAuthenticated, ))
class RegularGradesListView(APIView):
    def get(self, request):
        subject = self.request.query_params.get('subjectID')
        student = self.request.query_params.get('studentID')
        grades = models.regularGrade.objects.filter(subjectID = subject, studentID = student)
        data = serializers.RegularGradeSerializer(grades, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = serializers.RegularGradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
