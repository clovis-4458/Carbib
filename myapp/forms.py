from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Candidates, Countries, Jobs, Agents


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='Password'
    )


class CandidateApplicationForm(forms.ModelForm):

    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))

    # Personal / Biodata fields
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nin_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    passport_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    place_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    religion = forms.ChoiceField(
        choices=[('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Judaism', 'Judaism'),
                 ('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Other', 'Other'), ('None', 'None')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    marital_status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_of_children = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), required=False)
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tribe = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    clan = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    working_experience = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country_worked = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Documents
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    passport_copy = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    full_photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    medical_copy = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    interpol = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    # Place of origin
    place_of_origin_village = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    place_of_origin_parish = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    place_of_origin_subcounty = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    place_of_origin_county = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    place_of_origin_district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Present address
    present_address_village = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    present_address_parish = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    present_address_subcounty = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    present_address_county = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    present_address_district = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Next of Kin
    next_of_kin_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    next_of_kin_relationship = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    next_of_kin_contact = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    next_of_kin_address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Education
    education_level = forms.ChoiceField(
        required=False,
        choices=[('PhD', 'PhD'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors'),
                 ('Diploma', 'Diploma'), ('Certificate', 'Certificate'), ('UACE', 'UACE'),
                 ('UCE', 'UCE'), ('PLE', 'PLE'), ('None', 'None')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Job-related
    job_applied = forms.ModelChoiceField(
        queryset=Jobs.objects.filter(status='open').order_by('-date_posted'),
        label='Job Applied For',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    job_location = forms.ModelChoiceField(
        queryset=Countries.objects.all(),
        label='Job Location',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    referral_info = forms.ModelChoiceField(
        queryset=Agents.objects.all(),
        required=False,
        label='Agent / Referral',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Candidates
        fields = [
            'full_name', 'nin_number', 'passport_number', 'date_of_birth', 'place_of_birth',
            'religion', 'marital_status', 'no_of_children', 'email', 'phone_number',
            'gender', 'tribe', 'clan', 'profile_picture', 'passport_copy', 'full_photo',
            'medical_copy', 'interpol',
            'present_address_village','present_address_parish','present_address_subcounty',
            'present_address_county','present_address_district',
            'working_experience','country_worked',
            'job_applied','job_location','referral_info'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
