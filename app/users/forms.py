from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django import forms
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()
# profile

        
from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
    # Fayl yuklash uchun ImageField (noto'g'ri foydalanilgan edi)
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'id': "fileInputDragDrop",
            "type": "file",
            "class": "sr-only",
            "aria-describedby": "validFileFormats"
        }),
        required=False  # Fayl yuklashni majburiy emas qilish
    )
    
    # Matnli maydon uchun to'g'ri widget
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': "O'zingiz haqida...",
            'class': "mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800"
        }),
        required=False  # Bio majburiy emas
    )
    
    # Oddiy matnli maydonlar uchun CharField va TextInput
    first_name = forms.CharField(
        label='Ism',
        widget=forms.TextInput(attrs={
            'placeholder': "Ism",
            'type': 'text',
            'class': "bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5"
        }),
        required=False
    )
    
    last_name = forms.CharField(
        label='Familiya',
        widget=forms.TextInput(attrs={
            'placeholder': "Familiya",
            'type': 'text',
            'class': "bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5"
        }),
        required=False
    )
    
    # Raqamli maydon uchun IntegerField va TextInput
    age = forms.IntegerField(
        label='Yosh',
        widget=forms.NumberInput(attrs={
            'placeholder': "Yosh",
            'type': 'number',
            'class': "bg-indigo-50 border border-indigo-300 text-indigo-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5"
        }),
        required=False  # Yosh majburiy emas
    )

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'image', 'bio']


class LoginForm(forms.Form):
    email=forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder':"name@mail.com",'class':"peer h-full w-full rounded-md border border-blue-gray-200 border-t-transparent !border-t-blue-gray-200 bg-transparent px-3 py-3 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:!border-t-gray-900 focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50"}))
    password=forms.CharField(label='parol', widget=forms.PasswordInput(attrs={'placeholder':"**********",'class':"peer h-full w-full rounded-md border border-blue-gray-200 border-t-transparent !border-t-blue-gray-200 bg-transparent px-3 py-3 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:!border-t-gray-900 focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50"}))
    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cleaned_data['password2']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

