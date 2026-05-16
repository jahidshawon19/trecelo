from django.db import models
from django.contrib.auth.models import User


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


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    maker = models.ForeignKey(
        StaffProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Maker Name",
    )

    # Documents
    documents = models.FileField(upload_to='products/documents/', blank=True, null=True)

    # Technical Specifications
    gg = models.TextField(verbose_name="GG", blank=True)
    end_ply = models.IntegerField(default=0)
    weight = models.FloatField(default=0.0)
    yarn_composition = models.TextField(blank=True)
    description = models.TextField(blank=True)
    challenge_in = models.TextField(blank=True)

    # Dates and SMVs
    submission_date = models.DateField(null=True, blank=True)
    knitting_smv = models.IntegerField(default=0)
    linking_smv = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/')
    caption = models.CharField(max_length=120, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['uploaded_at']

    def __str__(self):
        return f"Image for {self.product.product_name}"
