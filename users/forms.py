from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserOurRegistration, self).__init__(*args, **kwargs)
        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# class ProfileImage(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ProfileImage, self).__init__(*args, **kwargs)
#         self.fields['img'].label = "Изображение профиля"
#         # self.fields['img'].widget.attrs.update({'class': 'form-section'})
#
#     class Meta:
#         model = Profile
#         fields = ['img']
