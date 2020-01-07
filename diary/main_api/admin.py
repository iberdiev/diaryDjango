from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, JkitepSchools, Cohort, Student, Subject, Teacher, regularGrade
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'name','user_role']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('user_role',),
        }),
    )
    fieldsets = (
        (('CustomUser'), {'fields': ('user_role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(JkitepSchools)
admin.site.register(Cohort)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(regularGrade)
