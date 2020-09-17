from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'name',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', )

class CustomUserPasswordChangeForm(SetPasswordForm):

    class Meta:
        model = CustomUser
        fields = ()