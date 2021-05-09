from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class About(models.Model):
    aboutTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="About",
        default="About",
        help_text="Maximum 50 character, unique.")

    aboutContent = RichTextField(
        verbose_name="About Content")

    aboutImage = models.ImageField(
        upload_to="about/en/",
        default="about/default_about_image.svg",
        verbose_name="About Image")

    def __str__(self):
        return self.aboutTitle

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Contact(models.Model):
    contactTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Contact",
        default="Contact",
        help_text="Maximum 50 character, unique.")

    address = RichTextField(
        verbose_name="Address")

    googleMap = models.TextField(
        verbose_name="Google Maps iFrame Link",
        help_text="Paste Google Maps iFrame link here.")

    phoneOne = models.CharField(
        max_length=20,
        verbose_name="Phone Number",
        help_text="This field is required.")

    phoneTwo = models.CharField(
        max_length=20,
        verbose_name="Phone Number",
        null=True, blank=True)

    phoneThree = models.CharField(
        max_length=20,
        verbose_name="Phone Number",
        null=True,
        blank=True)

    emailOne = models.CharField(
        max_length=40,
        verbose_name="E-Mail",
        help_text="This field is required.")

    emailTwo = models.CharField(
        max_length=40,
        verbose_name="E-Mail",
        null=True,
        blank=True)

    emailThree = models.CharField(
        max_length=40,
        verbose_name="E-Mail",
        null=True,
        blank=True)

    facebook = models.CharField(
        max_length=100,
        verbose_name="Facebook Link",
        null=True,
        blank=True,
        help_text="Paste Facebook link here.")

    twitter = models.CharField(
        max_length=100,
        verbose_name="Twitter Link",
        null=True,
        blank=True,
        help_text="Paste Twitter link here.")

    instagram = models.CharField(
        max_length=100,
        verbose_name="Instagram Link",
        null=True,
        blank=True,
        help_text="Paste Instagram link here.")

    youtube = models.CharField(
        max_length=100,
        verbose_name="Youtube Link",
        null=True,
        blank=True,
        help_text="Paste Youtube link here.")

    linkedin = models.CharField(
        max_length=100,
        verbose_name="Linkedin Link",
        null=True,
        blank=True,
        help_text="Paste Linkedin link here.")

    def __str__(self):
        return self.contactTitle

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'


class Faq(models.Model):
    faqTitle = models.TextField(
        verbose_name="Question")

    faqContent = models.TextField(
        verbose_name="Answer")

    faqSlug = models.SlugField(
        verbose_name="Question Slug",
        help_text="Url format of the Question, unique.")

    def __str__(self):
        return self.faqTitle

    class Meta:
        verbose_name = 'Frequently Asked Question'
        verbose_name_plural = 'Frequently Asked Questions'


class PrivacyPolicy(models.Model):
    policyTitle = models.CharField(
        max_length=50,
        verbose_name="Policy Title",
        help_text="Maximum 50 character, unique.",
        default="Privacy Policy")

    policyContent = RichTextField(
        verbose_name="Policy Content")

    def __str__(self):
        return self.policyTitle

    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policies'
