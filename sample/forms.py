from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Brand, Buyer, Category, ChallengeIn, GG, Sample, StaffProfile


class NoPathFileInput(forms.ClearableFileInput):
    """ClearableFileInput that hides the 'Currently: <path>' text on edit forms."""
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['is_initial'] = False
        return context


class BuyerForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Buyer
        fields = ['buyer_name', 'brand']
        widgets = {
            'brand': forms.SelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk:
            username = cleaned_data.get('username')
            if not username:
                self.add_error('username', 'Username is required.')
            elif User.objects.filter(username=username).exists():
                self.add_error('username', 'A user with that username already exists. Please choose a different username.')
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
            buyer.password_plain = self.cleaned_data['password']
        elif self.cleaned_data.get('password'):
            buyer.user.set_password(self.cleaned_data['password'])
            buyer.user.save()
            buyer.password_plain = self.cleaned_data['password']
        if commit:
            buyer.save()
            self.save_m2m()   # saves brand M2M assignments
        return buyer


class StaffForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = StaffProfile
        fields = [
            'maker_name',
            'emp_id',
            'role',
            'designation',
            'address',
            'nid',
            'phone_number',
            'profile_picture',
        ]
        widgets = {
            'profile_picture': NoPathFileInput(attrs={'accept': 'image/*'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk:
            username = cleaned_data.get('username')
            if not username:
                self.add_error('username', 'Username is required.')
            elif User.objects.filter(username=username).exists():
                self.add_error('username', 'A user with that username already exists. Please choose a different username.')
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
            staff.password_plain = self.cleaned_data['password']
        else:
            staff = super().save(commit=False)
            if self.cleaned_data.get('password'):
                staff.user.set_password(self.cleaned_data['password'])
                staff.user.save()
                staff.password_plain = self.cleaned_data['password']
        if commit:
            staff.save()
        return staff


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = [
            'style_number',
            'sample_type',
            'color',
            'season',
            'status',
            'category',
            'front_part_image',
            'back_part_image',
            'documents',
            'brand',
            'buyer',
            'gg',
            'size',
            'weight',
            'yarn_composition',
            'description',
            'submission_date',
            'challenge_in',
            'maker',
        ]
        widgets = {
            'submission_date': forms.DateInput(attrs={'type': 'date'}),
            'front_part_image': NoPathFileInput(attrs={'accept': 'image/*'}),
            'back_part_image': NoPathFileInput(attrs={'accept': 'image/*'}),
            'category': forms.SelectMultiple(),
            'brand': forms.SelectMultiple(),
            'gg': forms.SelectMultiple(),
            'challenge_in': forms.CheckboxSelectMultiple(),
            'maker': forms.CheckboxSelectMultiple(),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'origin', 'logo']
        widgets = {
            'logo': NoPathFileInput(attrs={'accept': 'image/*'}),
        }


class GGForm(forms.ModelForm):
    class Meta:
        model = GG
        fields = ['title']


class ChallengeInForm(forms.ModelForm):
    class Meta:
        model = ChallengeIn
        fields = ['title']
