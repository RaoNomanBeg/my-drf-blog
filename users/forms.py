from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # emial= forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model=User
        fields=('username','email','password1','password2')

        # def __init__(self, *args, **kwargs):
        #     super(SignUpForm, self).__init__(*args, **kwargs)
        #     self.fields['username'].help_text = ""
        #     self.fields['email'].help_text =""
        #     self.fields['password1'].help_text = ""
        #     self.fields['password2'].help_text = ""

        # def __init__(self,*args,**kwargs):
        #    super(SignUpForm, self).__init__(*args,**kwargs)
        #    self.fields['username'].help_text=None
        #    self.fields['email'].help_text=None
        #    self.fields['password1'].help_text=None
        #    self.fields['password2'].help_text=None
