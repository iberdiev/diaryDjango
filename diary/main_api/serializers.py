from rest_framework import serializers
from . import models
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from django.utils.timezone import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username','user_role', 'name',)

    # def create(self, validated_data):
    #     user = super(UserSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

class ChangeTimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Timetable
        fields = ('startTime','endTime', 'teacher','homework',)


class ChangeRegularGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.regularGrade
        fields = ("pk", "mark",)

class DeleteRegularGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.regularGrade
        fields = ("pk",)


class CustomRegisterSerializer(RegisterSerializer):

    user_role = serializers.IntegerField()

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['user_role'] = self.validated_data.get('user_role', '')
        data_dict['password1'] = self.validated_data.get('password1', '')
        data_dict['password2'] = self.validated_data.get('password2', '')
        return data_dict


class FilteredRegularGradeListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(studentID=self.context["studentID"])
        return super(FilteredRegularGradeListSerializer, self).to_representation(data)

class FilteredRegularGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.regularGrade
        fields = ('mark','studentID','lesson',)
        list_serializer_class = FilteredRegularGradeListSerializer

class RegularGradeSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.regularGrade
        fields = ('mark','lesson',"date",)
    def get_date(self, grade):
        return grade.lesson.date

class StudentProfileSerializer(serializers.ModelSerializer):
    parentName = serializers.SerializerMethodField(read_only=True)
    parentPhoneNumber = serializers.SerializerMethodField(read_only=True)
    className = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Student
        fields = ('studentName','phoneNumber','parentName','parentPhoneNumber','className',)
    def get_parentName(self, student):
        return student.parent.name
    def get_parentPhoneNumber(self, student):
        return student.parent.phoneNumber
    def get_className(self, student):
        return student.cohort.class_name

class UniqueCohortsBySubjectsForTeacherList(serializers.ListSerializer):

    def to_representation(self, data):

        data = data.distinct()
        return super(UniqueCohortsBySubjectsForTeacherList, self).to_representation(data)

class UniqueCohortsBySubjectsForTeacher(serializers.ModelSerializer):
    cohortName = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = models.Subject
        fields = ('cohortName', 'cohortID',)
        list_serializer_class = UniqueCohortsBySubjectsForTeacherList

    def get_cohortName(self, subject):
        return subject.cohortID.class_name


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
        fields = ('class_name','pk', 'mainTeacherID',)
        depth = 1

class CohortSerializerOnlyNameAndID(serializers.ModelSerializer):
    cohortName = serializers.SerializerMethodField(read_only=True)
    cohortID = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Cohort
        fields = ('cohortName','cohortID',)
    def get_cohortName(self, cohort):
        return cohort.class_name
    def get_cohortID(self, cohort):
        return cohort.pk


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('teacherName','pk',)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('subjectName', 'teacherID', 'pk',)
        depth = 1

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('studentName','pk','cohort',)
#33dfghgfsdfg4wcw45crg#33dfghgfsdfg4wcw45crg#33dfghgfsdfg4wcw45crg#33dfghgfsdfg4wcw45crg#33dfghgfsdfg4wcw45crg

class FinalGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.finalGrade
        fields = ['type','mark', 'pk','studentID', 'subjectID']

class ChangeFinalGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.finalGrade
        fields = ['mark']

class StudentFinalGradesSerializer(serializers.ModelSerializer):
    finalGrades = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Student
        fields = ('studentName','pk','cohort','finalGrades',)
    def get_finalGrades(self, student):
        grades = models.finalGrade.objects.filter(studentID=student,subjectID=self.context["subjectID"])
        serializer = FinalGradeSerializer(instance=grades, many=True)
        return serializer.data

# class RegularGradesBySubjectListSerializer(serializers.ListSerializer):
#
#     def to_representation(self, data):
#         # print(self.context["subjectID"])
#         # data = data.filter(subjectID=self.context["subjectID"])
#         data = data
#         return super(RegularGradesBySubjectListSerializer, self).to_representation(data)

class RegularGradesBySubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.regularGrade
        fields = ('pk','mark', 'lesson','type',)
        # list_serializer_class = RegularGradesBySubjectListSerializer
        depth = 1

class StudentGradesOneSubjectSerializer(serializers.ModelSerializer):
    regularGrades = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Student
        fields = ('studentName','pk','cohort','regularGrades',)
    def get_regularGrades(self, student):
        # print(datetime.today()- datetime.timedelta(days=13))
        grades = models.regularGrade.objects.filter(studentID=student,lesson__subjectID=self.context["subjectID"],type=6, lesson__date__lte=datetime.today())
        serializer = RegularGradesBySubjectSerializer(instance=grades, many=True)
        return serializer.data

#33dfghgfsdfg4wcw45crg#33dfghgfsdfg4wcw45crg#33dfghgfsdfg4wcw45crg#33dfghgfsdfg4wcw45crg#33dfghgfsdfg4wcw45crg

class TimetableWithOneStudentSerializer(serializers.ModelSerializer):
    subjectName = serializers.SerializerMethodField(read_only=True)
    regularGrades = FilteredRegularGradeSerializer(many=True)

    class Meta:
        model = models.Timetable
        fields = ('subjectID', 'cohortID', 'date', 'startTime', 'endTime', 'homework','teacher','subjectName', 'regularGrades',)

    def get_subjectName(self, timetable):
        return timetable.subjectID.subjectName

class TimetableSerializer(serializers.ModelSerializer):
    subjectName = serializers.SerializerMethodField(read_only=True)
    teacherName = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Timetable
        fields = ('pk','subjectID', 'cohortID', 'date', 'startTime', 'endTime', 'homework','teacher','subjectName','teacherName',)
    def get_subjectName(self, timetable):
        return timetable.subjectID.subjectName
    def get_teacherName(self, timetable):
        return timetable.teacher.teacherName


#jhaksldfjiuasdhfoshdfui
# class RegularGradesForOneCohortBySubjectList(serializers.ListSerializer):
#
#     def to_representation(self, data):
#         data = data.filter(data)
#         return super(RegularGradesForOneCohortBySubjectList, self).to_representation(data)


class RegularGradesForOneCohortBySubject(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Student
        fields = ('lesson', 'studentID', 'teacherID', 'mark', 'date',)
    def get_date(self, regularGrade):
        return regularGrade.lesson.date


class TimetableForTeacherSerializer(serializers.ModelSerializer):
    subjectName = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Timetable
        fields = ('subjectID', 'cohortID', 'date', 'startTime', 'endTime', 'homework','teacher','subjectName', )
    def get_subjectName(self, timetable):
        return timetable.subjectID.subjectName

class FilteredTimetableListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(date=self.context["date"])
        return super(FilteredTimetableListSerializer, self).to_representation(data)

class FilteredTimetableSerializer(serializers.ModelSerializer):
    subjectName = serializers.SerializerMethodField(read_only=True)
    className = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Timetable
        fields = ('subjectID', 'cohortID', 'date', 'startTime', 'endTime', 'homework','teacher','subjectName','className', )
        list_serializer_class = FilteredTimetableListSerializer
    def get_subjectName(self, timetable):
        return timetable.subjectID.subjectName
    def get_className(self, timetable):
        return timetable.cohortID.class_name

class JkitepSchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JkitepSchools
        fields = ('schoolsid', 'type_ownership', 'name', 'school_code',)

class SubjectsRegularFinalGradesSerializer(serializers.ModelSerializer):
    regularGrades = serializers.SerializerMethodField(read_only=True)
    finalGrades = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Subject
        fields = ("subjectName", "pk", "regularGrades", "finalGrades")

    def get_regularGrades(self, subject):
        grades = models.regularGrade.objects.filter(lesson__subjectID=subject.pk, studentID=self.context["studentID"])
        serializer = RegularGradeSerializer(instance=grades, many=True)
        return serializer.data

    def get_finalGrades(self, subject):
        grades = models.finalGrade.objects.filter(subjectID=subject.pk, studentID=self.context["studentID"])
        serializer = FinalGradeSerializer(instance=grades, many=True)
        return serializer.data
