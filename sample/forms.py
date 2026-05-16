from django import forms
from django.contrib.auth.models import User
from .models import Buyer, Product, StaffProfile


class BuyerForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Buyer
        fields = ['buyer_name']

    def clean(self):
        cleaned_data = super().clean()
        # Username and password are only required when creating a new buyer
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


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        if not data:
            return []
        if not isinstance(data, (list, tuple)):
            data = [data]
        return [super(MultipleImageField, self).clean(f, initial) for f in data]


class ProductForm(forms.ModelForm):
    images = MultipleImageField(
        required=False,
        label='Product Images',
        widget=MultipleFileInput(attrs={'accept': 'image/*'}),
    )

    class Meta:
        model = Product
        fields = [
            'product_name',
            'buyer',
            'maker',
            'documents',
            'gg',
            'end_ply',
            'weight',
            'yarn_composition',
            'description',
            'challenge_in',
            'submission_date',
            'knitting_smv',
            'linking_smv',
        ]
        widgets = {
            'submission_date': forms.DateInput(attrs={'type': 'date'}),
        }
