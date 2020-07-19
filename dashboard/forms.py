from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Athelete, plan, KB


class AtheleteRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['name', 'surname' ,'username', 'email', 'password1', 'password2']

class PracticeRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PlanUpdateMonday(forms.ModelForm):
    class Meta:
        model = plan
        fields = ['Monday_Title', 'Monday_Description', 'Monday_Video_url']

class PlanUpdateTuesday(forms.ModelForm):
    class Meta:
        model = plan
        fields = ['Tuesday_Title', 'Tuesday_Description', 'Tuesday_Video_url']

class PlanUpdateWednesday(forms.ModelForm):
    class Meta:
        model = plan
        fields = ['Wednesday_Title', 'Wednesday_Description', 'Wednesday_Video_url']

class PlanUpdateThursday(forms.ModelForm):
    class Meta:
        model = plan
        fields = ['Thursday_Title', 'Thursday_Description', 'Thursday_Video_url']

class PlanUpdateFriday(forms.ModelForm):
    class Meta:
        model = plan
        fields = ['Friday_Title', 'Friday_Description', 'Friday_Video_url']

class PlanUpdateSaturday(forms.ModelForm):
    class Meta:
        model = plan
        fields = ['Saturday_Title', 'Saturday_Description', 'Saturday_Video_url']

class PlanUpdateSunday(forms.ModelForm):
    class Meta:
        model = plan
        fields = ['Sunday_Title', 'Sunday_Description', 'Sunday_Video_url']

class KBUpdate(forms.ModelForm):
    class Meta:
        model = KB
        fields = ['url']

class AtheleteUpdateForm(forms.ModelForm):
    class Meta:
        model = Athelete
        fields = ['profile_pic', 'contact_number', 'sport']