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

    STATUS_PENDING  = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_DRAFT    = 'draft'
    STATUS_CHOICES  = [
        (STATUS_PENDING,  'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_DRAFT,    'Draft'),
    ]

    style_number = models.CharField(max_length=100, blank=True, verbose_name="Style Number")
    sample_type  = models.CharField(max_length=100, blank=True, verbose_name="Sample Type")
    color        = models.CharField(max_length=100, blank=True, verbose_name="Color")
    season       = models.IntegerField(null=True, blank=True, verbose_name="Season")
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT, verbose_name="Status")
    category = models.ManyToManyField(Category, blank=True)
    brand = models.ManyToManyField(Brand, blank=True, verbose_name="Brand Name")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    maker = models.ForeignKey(
        StaffProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Maker Name",
    )

    # Fixed image slots
    front_part_image = models.ImageField(upload_to='samples/front/', blank=True, null=True, verbose_name="Front Part Image")
    back_part_image = models.ImageField(upload_to='samples/back/', blank=True, null=True, verbose_name="Back Part Image")

    # Document
    documents = models.FileField(upload_to='samples/documents/', blank=True, null=True)

    # Technical Specifications
    gg = models.ManyToManyField(GG, blank=True, verbose_name="GG")
    weight = models.CharField(max_length=100, blank=True, verbose_name="Weight")
    yarn_composition = models.CharField(max_length=255, blank=True, verbose_name="Yarn Composition")
    description = models.TextField(blank=True)
    challenge_in = models.ManyToManyField(ChallengeIn, blank=True, verbose_name="Challenge In")
    submission_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.style_number or f"Sample #{self.pk}"


class ChallengeImage(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='challenge_images')
    image = models.ImageField(upload_to='samples/challenge/')

    def __str__(self):
        return f"Challenge image for {self.sample.product_name}"
