from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'
    def __int__(self):
        self.fields['password1'].required = True
        self.fields['password2'].required = True
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        # clean_email = self.cleaned_data["email"]
        if commit:
            user.save()

        # custom_user = CustomUser()
        # custom_user.id = user
        # custom_user.save()
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
