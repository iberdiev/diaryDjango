from django.urls import include, path
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('login/', views.CustomLoginView.as_view()),
    path('get_cohorts/', views.CohortsView.as_view()),
    path('students/', views.StudentsListView.as_view()),
    path('subjects/', views.SubjectsListView.as_view()),
    path('teachers/', views.TeachersListView.as_view()),
    path('changeTeacher/', views.ChangeTeacherOfSubject.as_view()),


    path('mainCohorts/', views.MainCohortList.as_view()),
    path('givenSubjectsOfTeacher/', views.givenSubjectsOfTeacher.as_view()),
    path('givenSubjectsOfTeacherStudentListView/', views.GivenSubjectStudentListView.as_view()),
    path('regularGrades/', views.RegularGradesListView.as_view()),
    path('timetableByCohort/', views.TimetableByCohortView.as_view()),
    path('timetableByTeacher/', views.TimetableByTeacherView.as_view()),
    # path('cohortsRelatedToTeacher/', views.CohortsRelatedToTeacher.as_view()),


    path('getTheChild/', views.getTheChild.as_view()),
]
