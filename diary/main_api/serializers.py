from rest_framework import serializers
from . import models
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username','user_role')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CustomRegisterSerializer(RegisterSerializer):

    user_role = serializers.IntegerField()

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['user_role'] = self.validated_data.get('user_role', '')
        return data_dict

class RegularGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.regularGrade
        fields = ('mark','pub_date','studentID','subjectID',)

class SubjectCohortSerializer(serializers.ModelSerializer):
    cohortName = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Subject
        fields = ('subjectName', 'teacherID', 'pk','cohortName')
    def get_cohortName(self, subject):
        return subject.cohortID.class_name

class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cohort
        fields = ('class_name','pk',)

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('teacherName','pk',)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('subjectName', 'teacherID', 'pk',)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('studentName','pk',)

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Timetable
        fields = ('subjectID', 'cohortID', 'date', 'startTime', 'endTime', 'homework',)

class JkitepSchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JkitepSchools
        fields = ('schoolsid', 'type_ownership', 'name', 'school_code' )
