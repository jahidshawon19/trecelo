import io
import os

from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User
from PIL import Image as PilImage


def _compress_image_field(instance, field_name, max_px, quality=82):
    """
    Resize + recompress an ImageField's file in-place on disk.

    - Images larger than max_px on either dimension are scaled down
      (aspect ratio preserved via thumbnail).
    - Images with an alpha channel (logos/PNGs) are saved as optimised PNG.
    - Everything else is converted to RGB and saved as JPEG at `quality`.
    - Already-small files under 100 KB that don't need resizing are left alone.
    """
    field = getattr(instance, field_name)
    if not field:
        return
    try:
        path = field.path
        img = PilImage.open(path)
        orig_w, orig_h = img.size
        needs_resize = orig_w > max_px or orig_h > max_px
        file_size = os.path.getsize(path)
        needs_compress = file_size > 100 * 1024  # > 100 KB

        if not needs_resize and not needs_compress:
            return  # already small enough, skip

        if needs_resize:
            img.thumbnail((max_px, max_px), PilImage.LANCZOS)

        has_alpha = img.mode in ('RGBA', 'LA', 'P')
        buf = io.BytesIO()
        if has_alpha:
            if img.mode == 'P':
                img = img.convert('RGBA')
            img.save(buf, format='PNG', optimize=True)
        else:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(buf, format='JPEG', quality=quality, optimize=True)

        buf.seek(0)
        with open(path, 'wb') as f:
            f.write(buf.read())
    except Exception:
        pass  # never break a save over image compression


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    COUNTRY_CHOICES = [
        ('Afghanistan',          '🇦🇫  Afghanistan'),
        ('Albania',              '🇦🇱  Albania'),
        ('Algeria',              '🇩🇿  Algeria'),
        ('Argentina',            '🇦🇷  Argentina'),
        ('Australia',            '🇦🇺  Australia'),
        ('Austria',              '🇦🇹  Austria'),
        ('Azerbaijan',           '🇦🇿  Azerbaijan'),
        ('Bangladesh',           '🇧🇩  Bangladesh'),
        ('Belgium',              '🇧🇪  Belgium'),
        ('Bolivia',              '🇧🇴  Bolivia'),
        ('Brazil',               '🇧🇷  Brazil'),
        ('Bulgaria',             '🇧🇬  Bulgaria'),
        ('Cambodia',             '🇰🇭  Cambodia'),
        ('Canada',               '🇨🇦  Canada'),
        ('Chile',                '🇨🇱  Chile'),
        ('China',                '🇨🇳  China'),
        ('Colombia',             '🇨🇴  Colombia'),
        ('Croatia',              '🇭🇷  Croatia'),
        ('Czech Republic',       '🇨🇿  Czech Republic'),
        ('Denmark',              '🇩🇰  Denmark'),
        ('Ecuador',              '🇪🇨  Ecuador'),
        ('Egypt',                '🇪🇬  Egypt'),
        ('Ethiopia',             '🇪🇹  Ethiopia'),
        ('Finland',              '🇫🇮  Finland'),
        ('France',               '🇫🇷  France'),
        ('Germany',              '🇩🇪  Germany'),
        ('Ghana',                '🇬🇭  Ghana'),
        ('Greece',               '🇬🇷  Greece'),
        ('Guatemala',            '🇬🇹  Guatemala'),
        ('Honduras',             '🇭🇳  Honduras'),
        ('Hong Kong',            '🇭🇰  Hong Kong'),
        ('Hungary',              '🇭🇺  Hungary'),
        ('India',                '🇮🇳  India'),
        ('Indonesia',            '🇮🇩  Indonesia'),
        ('Iran',                 '🇮🇷  Iran'),
        ('Iraq',                 '🇮🇶  Iraq'),
        ('Ireland',              '🇮🇪  Ireland'),
        ('Israel',               '🇮🇱  Israel'),
        ('Italy',                '🇮🇹  Italy'),
        ('Japan',                '🇯🇵  Japan'),
        ('Jordan',               '🇯🇴  Jordan'),
        ('Kazakhstan',           '🇰🇿  Kazakhstan'),
        ('Kenya',                '🇰🇪  Kenya'),
        ('South Korea',          '🇰🇷  South Korea'),
        ('Kuwait',               '🇰🇼  Kuwait'),
        ('Laos',                 '🇱🇦  Laos'),
        ('Lebanon',              '🇱🇧  Lebanon'),
        ('Libya',                '🇱🇾  Libya'),
        ('Malaysia',             '🇲🇾  Malaysia'),
        ('Mexico',               '🇲🇽  Mexico'),
        ('Morocco',              '🇲🇦  Morocco'),
        ('Myanmar',              '🇲🇲  Myanmar'),
        ('Nepal',                '🇳🇵  Nepal'),
        ('Netherlands',          '🇳🇱  Netherlands'),
        ('New Zealand',          '🇳🇿  New Zealand'),
        ('Nigeria',              '🇳🇬  Nigeria'),
        ('Norway',               '🇳🇴  Norway'),
        ('Oman',                 '🇴🇲  Oman'),
        ('Pakistan',             '🇵🇰  Pakistan'),
        ('Peru',                 '🇵🇪  Peru'),
        ('Philippines',          '🇵🇭  Philippines'),
        ('Poland',               '🇵🇱  Poland'),
        ('Portugal',             '🇵🇹  Portugal'),
        ('Qatar',                '🇶🇦  Qatar'),
        ('Romania',              '🇷🇴  Romania'),
        ('Russia',               '🇷🇺  Russia'),
        ('Saudi Arabia',         '🇸🇦  Saudi Arabia'),
        ('Senegal',              '🇸🇳  Senegal'),
        ('Singapore',            '🇸🇬  Singapore'),
        ('South Africa',         '🇿🇦  South Africa'),
        ('Spain',                '🇪🇸  Spain'),
        ('Sri Lanka',            '🇱🇰  Sri Lanka'),
        ('Sweden',               '🇸🇪  Sweden'),
        ('Switzerland',          '🇨🇭  Switzerland'),
        ('Taiwan',               '🇹🇼  Taiwan'),
        ('Tanzania',             '🇹🇿  Tanzania'),
        ('Thailand',             '🇹🇭  Thailand'),
        ('Tunisia',              '🇹🇳  Tunisia'),
        ('Turkey',               '🇹🇷  Turkey'),
        ('Uganda',               '🇺🇬  Uganda'),
        ('Ukraine',              '🇺🇦  Ukraine'),
        ('United Arab Emirates', '🇦🇪  United Arab Emirates'),
        ('United Kingdom',       '🇬🇧  United Kingdom'),
        ('United States',        '🇺🇸  United States'),
        ('Uruguay',              '🇺🇾  Uruguay'),
        ('Uzbekistan',           '🇺🇿  Uzbekistan'),
        ('Venezuela',            '🇻🇪  Venezuela'),
        ('Vietnam',              '🇻🇳  Vietnam'),
        ('Yemen',                '🇾🇪  Yemen'),
        ('Zimbabwe',             '🇿🇼  Zimbabwe'),
    ]

    name   = models.CharField(max_length=100)
    origin = models.CharField(max_length=100, blank=True, choices=COUNTRY_CHOICES, verbose_name='Origin Country')
    logo   = models.ImageField(upload_to='brands/logos/', blank=True, null=True, verbose_name='Brand Logo')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        _compress_image_field(self, 'logo', max_px=400)

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
    brand = models.ManyToManyField('Brand', blank=True, verbose_name='Brands')
    password_plain = models.CharField(max_length=128, blank=True, verbose_name='Password')

    def __str__(self):
        return self.buyer_name


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    maker_name = models.CharField(max_length=100, blank=True, verbose_name='Maker Name')
    emp_id = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    address = models.TextField()
    nid = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    profile_picture = models.ImageField(upload_to='staff/profiles/', blank=True, null=True, verbose_name='Profile Picture')
    password_plain = models.CharField(max_length=128, blank=True, verbose_name='Password')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        _compress_image_field(self, 'profile_picture', max_px=500)

    def __str__(self):
        return self.user.username


class Sample(models.Model):

    STATUS_PENDING  = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_DRAFT    = 'draft'
    STATUS_REJECTED = 'rejected'
    STATUS_CHOICES  = [
        (STATUS_PENDING,  'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_DRAFT,    'Draft'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    style_number = models.CharField(max_length=100, blank=True, verbose_name="Style Number")
    sample_type  = models.CharField(max_length=100, blank=True, verbose_name="Sample Type")
    color        = models.CharField(max_length=100, blank=True, verbose_name="Color")
    season       = models.IntegerField(null=True, blank=True, verbose_name="Season")
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT, verbose_name="Status")
    category = models.ManyToManyField(Category, blank=True)
    brand = models.ManyToManyField(Brand, blank=True, verbose_name="Brand Name")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    maker = models.ManyToManyField(
        StaffProfile,
        blank=True,
        verbose_name="Maker Name",
    )

    # Fixed image slots
    front_part_image = models.ImageField(upload_to='samples/front/', blank=True, null=True, verbose_name="Front Part Image")
    back_part_image = models.ImageField(upload_to='samples/back/', blank=True, null=True, verbose_name="Back Part Image")
    tech_pack = models.ImageField(upload_to='samples/tech_pack/', blank=True, null=True, verbose_name="Tech Pack")

    # Document
    documents = models.FileField(upload_to='samples/documents/', blank=True, null=True)

    # Technical Specifications
    gg = models.ManyToManyField(GG, blank=True, verbose_name="GG")
    size = models.CharField(max_length=100, blank=True, verbose_name="Size")
    weight = models.CharField(max_length=100, blank=True, verbose_name="Weight")
    yarn_composition = models.CharField(max_length=255, blank=True, verbose_name="Yarn Composition")
    yarn_consumption = models.CharField(max_length=255, blank=True, verbose_name="Yarn Consumption")
    moisture_level = models.CharField(max_length=100, blank=True, verbose_name="Moisture Level")
    description = models.TextField(blank=True)
    challenge_in = models.ManyToManyField(ChallengeIn, blank=True, verbose_name="Challenge In")
    submission_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        _compress_image_field(self, 'front_part_image', max_px=1200)
        _compress_image_field(self, 'back_part_image',  max_px=1200)
        _compress_image_field(self, 'tech_pack',        max_px=1200)

    def __str__(self):
        return self.style_number or f"Sample #{self.pk}"


class TopManagement(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name   = models.CharField(max_length=100, verbose_name='Full Name')
    department  = models.CharField(max_length=100, verbose_name='Department')
    designation = models.CharField(max_length=100, verbose_name='Designation')
    password_plain = models.CharField(max_length=128, blank=True, verbose_name='Password')

    class Meta:
        verbose_name        = 'Top Management'
        verbose_name_plural = 'Top Management'

    def __str__(self):
        return self.full_name or self.user.username


class GeneralCustomer(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    password_plain = models.CharField(max_length=128, blank=True, verbose_name='Password')

    class Meta:
        verbose_name        = 'General Customer'
        verbose_name_plural = 'General Customers'

    def __str__(self):
        return self.user.username


class ChallengeImage(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='challenge_images')
    image = models.ImageField(upload_to='samples/challenge/')

    def __str__(self):
        return f"Challenge image for {self.sample.product_name}"
