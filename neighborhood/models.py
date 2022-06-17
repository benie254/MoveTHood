from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.core.mail import send_mail

# Create your models here.

class voter(models.Model):
	username = models.CharField(max_length=60)
	display_name = models.CharField(max_length=60)
	bio = models.CharField(max_length=60, null=True)
	# p_pic = CloudinaryField('image', null=True)
	created = models.DateTimeField(auto_now_add=True)

class User(AbstractBaseUser):
	username = models.CharField(max_length=40,unique=True)
	USERNAME_FIELD = 'username'
	first_name = models.CharField("first name", max_length=150, blank=True)
	last_name = models.CharField("last name", max_length=150, blank=True)
	email = models.EmailField("email address", blank=True)
	is_active = models.BooleanField("active", default=True, help_text=("Designates whether this user should be treated as active. "
																	   "Unselect this instead of deleting accounts."), )
	date_joined = models.DateTimeField("date joined", default=timezone.now)
	EMAIL_FIELD = "email"
	REQUIRED_FIELDS = ["email"]

	def clean(self):
		super().clean()
		self.email = self.__class__.objects.normalize_email(self.email)

	def get_full_name(self):
		"""
		Return the first_name plus the last_name, with a space in between.
		"""
		full_name = "%s %s" % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		"""Return the short name for the user."""
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		"""Send an email to this user."""
		send_mail(subject, message, from_email, [self.email], **kwargs)

