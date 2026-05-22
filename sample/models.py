from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GG(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'GG'
        verbose_name_plural = 'GGs'

    def __str__(self):
        return self.title


class ChallengeIn(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Challenge In'
        verbose_name_plural = 'Challenges In'

    def __str__(self):
        return self.title


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.buyer_name


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    address = models.TextField()
    nid = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Sample(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="Sample Name")
    style_number = models.CharField(max_length=100, blank=True, verbose_name="Style Number")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Brand Name")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    maker = models.ForeignKey(
        StaffProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Maker Name",
    )

    # Three fixed image slots
    front_part_image = models.ImageField(upload_to='samples/front/', blank=True, null=True, verbose_name="Front Part Image")
    back_part_image = models.ImageField(upload_to='samples/back/', blank=True, null=True, verbose_name="Back Part Image")
    challenge_part_image = models.ImageField(upload_to='samples/challenge/', blank=True, null=True, verbose_name="Challenge Part Image")

    # Document
    documents = models.FileField(upload_to='samples/documents/', blank=True, null=True)

    # Technical Specifications
    gg = models.ForeignKey(GG, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="GG")
    end_ply = models.IntegerField(default=0)
    weight = models.CharField(max_length=100, blank=True, verbose_name="Weight")
    yarn_composition = models.TextField(blank=True)
    description = models.TextField(blank=True)
    challenge_in = models.ForeignKey(ChallengeIn, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Challenge In")

    # Dates and SMVs
    submission_date = models.DateField(null=True, blank=True)
    knitting_smv = models.IntegerField(default=0)
    linking_smv = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
