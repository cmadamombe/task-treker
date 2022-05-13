from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm #We import the ModelForm class, which will do all the heavy lifting for us.

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """

class UserUpdateForm(ModelForm):  # UserUpdateForm class inherits from ModelForm.
    username = forms.CharField(required=False, disabled=True)
    email = forms.EmailField(required=False, disabled=True)
    first_name = forms.CharField(required=False, disabled=True)
    middle_name = forms.CharField(required=False, disabled=True)
    last_name = forms.CharField(required=False, disabled=True)
    is_superuser = forms.BooleanField(required=False, disabled=True)
    is_staff = forms.BooleanField(required=False, disabled=True)
    is_active = forms.BooleanField(required=False, disabled=True)
    is_admin = forms.BooleanField(required=False, disabled=True)
    date_joined = forms.CharField(required=False, disabled=True)

    class Meta:  # The ModelForm class has an internal Meta class which we use to pass in the metadata options the ModelForm class needs to render our form:
            model = User
            fields = ['username', 'email', 'first_name', 'middle_name', 'last_name', 'is_superuser', 'is_staff',
                      'is_active', 'is_admin', 'date_joined']
            help_texts = {
            'username': None,
            'is_superuser': None,
            }

