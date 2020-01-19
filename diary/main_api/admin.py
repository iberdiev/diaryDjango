from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (CustomUser,Cohort,Student,Subject,Teacher,regularGrade,Timetable,finalGrade,LastChangeInJkitepModtrackerBasic,
    JkitepSchools, JkitepSchoolclasses, JkitepSchoolstaff, JkitepContactdetails, JkitepCrmentity)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'name','user_role', 'created_date','phoneNumber','email','codeToResetPassword']
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {
    #         'fields': ('name','user_role','phoneNumber',),
    #     }),
    # )
    fieldsets = (
        (('CustomUser'), {'fields': ('name','user_role','phoneNumber','email',)}),
    )
    list_filter = ('user_role', )
    ordering = ('-created_date',)




admin.site.register(JkitepSchools)
admin.site.register(JkitepSchoolclasses)
admin.site.register(JkitepSchoolstaff)
admin.site.register(JkitepContactdetails)
admin.site.register(JkitepCrmentity)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cohort)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(regularGrade)
admin.site.register(Timetable)
admin.site.register(finalGrade)
admin.site.register(LastChangeInJkitepModtrackerBasic)
