from django import forms
from django.contrib.auth.models import User
from .models import Brand, Buyer, Category, ChallengeIn, GG, Sample, StaffProfile


class BuyerForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Buyer
        fields = ['buyer_name']

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk:
            if not cleaned_data.get('username'):
                self.add_error('username', 'Username is required.')
            if not cleaned_data.get('password'):
                self.add_error('password', 'Password is required.')
        return cleaned_data

    def save(self, commit=True):
        buyer = super().save(commit=False)
        if not self.instance.pk:
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password'],
            )
            buyer.user = user
        if commit:
            buyer.save()
        return buyer


class StaffForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = StaffProfile
        fields = [
            'emp_id',
            'role',
            'designation',
            'address',
            'nid',
            'phone_number',
        ]

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk:
            if not cleaned_data.get('username'):
                self.add_error('username', 'Username is required.')
            if not cleaned_data.get('password'):
                self.add_error('password', 'Password is required.')
        return cleaned_data

    def save(self, commit=True):
        if not self.instance.pk:
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password'],
            )
            user.is_staff = True
            user.save()
            staff = super().save(commit=False)
            staff.user = user
        else:
            staff = super().save(commit=False)
        if commit:
            staff.save()
        return staff


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = [
            'product_name',
            'style_number',
            'category',
            'front_part_image',
            'back_part_image',
            'documents',
            'brand',
            'buyer',
            'gg',
            'weight',
            'yarn_composition',
            'description',
            'submission_date',
            'challenge_in',
            'maker',

        ]
        widgets = {
            'submission_date': forms.DateInput(attrs={'type': 'date'}),
            'front_part_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'back_part_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


class GGForm(forms.ModelForm):
    class Meta:
        model = GG
        fields = ['title']


class ChallengeInForm(forms.ModelForm):
    class Meta:
        model = ChallengeIn
        fields = ['title']
