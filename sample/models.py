from django.db import models
from django.contrib.auth.models import User


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

    # Document
    documents = models.FileField(upload_to='samples/documents/', blank=True, null=True)

    # Technical Specifications
    gg = models.ManyToManyField(GG, blank=True, verbose_name="GG")
    size = models.CharField(max_length=100, blank=True, verbose_name="Size")
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
