from django import forms
from .models import post, Profile,Comment
from django.contrib.auth.models import User

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=post
        fields=(
            'title',
            'body',
            'status',
        )

class PostEditForm(forms.ModelForm):
    class Meta:
        model=post
        fields=(
            'title',
            'body',
            'status',
        )

class UserLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username here..'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password here..'}))




class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password here..'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password here..'}))
    class Meta:
        model = User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
        )
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password mismatch")
        return confirm_password


class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = User
        fields = {
                'username',
                'first_name',
                'last_name',
                'email',
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here !!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)
