from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django import forms
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import admin
from django.utils.safestring import mark_safe


class Specialization(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Specializations"
		ordering = ['name']

class CertNames(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Technical Certifications"
		ordering = ['name']


class Applicant(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	known_as  = models.CharField(max_length=100, help_text="Also Known As / Alias", null=True, blank=True)
	signup_time = models.DateTimeField(auto_now_add=True)
	nationality = CountryField(null=True, blank=True)
	add_nationality = CountryField(null=True, blank=True, verbose_name='Additional Residency', help_text="(optional)")
	STATUS_CHOICES =(
		('Citizen','Citizen'),
		('Permanent Resident','Permanent Resident'),
		('Work Permit/Visa', 'Work Permit/Visa'),
		)
	add_nat_status = models.CharField(max_length=60, null=True, blank=True, choices=STATUS_CHOICES, verbose_name='Additional Residency Status', help_text="e.g. PR, Citizen etc. (optional)")
	date_of_birth = models.DateField(null=True, blank=True)
	email = models.EmailField(verbose_name="Email Address", unique=True)
	confirm_email = models.EmailField(null=True, blank=True)
	contact_home = PhoneNumberField(null=True, blank=True)
	contact_mobile = PhoneNumberField()
	MARITAL_STATUS_CHOICES = (
		('SINGLE' , 'Single'),
		('MARRIED', 'Married'),
		('DIVORCED', 'Divorced'),
		('WIDOWED', 'Widowed'),
		)
	GENDER_CHOICES = (
		('MALE', 'Male'),
		('FEMALE', 'Female'),
		)
	marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
	gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True)
	address_line_1 = models.CharField(max_length=300, verbose_name="Address Line 1", null=True, blank=True)
	address_line_2 = models.CharField(max_length=300, null=True, blank=True, verbose_name="Address Line 2")
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=100, null=True, blank=True)
	postal_code = models.IntegerField(max_length=100, verbose_name="Postal Code", null=True, blank=True)
	country = CountryField(null=True, blank=True)
	abi_summary = models.TextField(verbose_name="ABI Professional Summary", null=True, blank=True)
	spec_summary = models.ManyToManyField(Specialization, null=True, blank=True, verbose_name="Specialization")
 	proposed_specialization = models.CharField(max_length=100, default='', help_text="Specialization to Appear on Generated CV (as per client request)", verbose_name="Proposed Title")
	language_proficiency = models.CharField(max_length=200, null=True, blank=True, verbose_name="Language Proficiency")
	computer_literacy = models.TextField(null=True, blank=True, verbose_name="Computer Literacy", help_text="e.g. Microsoft Office, Auto CAD, PDMS etc.")
	current_salary = models.CharField(max_length=50, null=True, blank=True, verbose_name="Current Drawn Salary USD $")
	notice_period = models.CharField(max_length=50, null=True, blank=True, verbose_name="Required Notice Period")
	current_pos =  models.CharField(max_length=50, null=True, blank=True, verbose_name="Current Position Held")
	whereabouts = models.CharField(max_length=50, null=True, blank=True, verbose_name="Current Whereabouts")
	OFFSHORE = (
		('YES', 'Yes'),
		('NO', 'No'),
		)
	offshore = models.CharField(max_length=3, choices=OFFSHORE, verbose_name="Willing to work Offshore?", null=True, blank=True)
	preferred_places = models.CharField(max_length=100, verbose_name="Preferred Places to Work", null=True, blank=True)
	describe_self = models.TextField(verbose_name="Self Description", null=True, blank=True)
	cv = models.FileField(upload_to='.', null=True, blank=True, verbose_name="Curriculum Vitae")
	blacklist = models.BooleanField(default=False)
	blacklist_reason = models.TextField(null=True, blank=True)
	declaration = models.BooleanField(verbose_name="Declared True")
	tos = models.BooleanField(verbose_name="TOS & Privacy Policy")

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = "CV Databases"
		verbose_name_plural = "CV Database"

	def full_name(self):
		return str(self.first_name) + " " + str(self.last_name)

	def cv_exists(self):
		if self.cv:
			html = '<a href="/media/%s" /><img src="/media/img/cv.jpg" /></a>' % self.cv
			return mark_safe(html)
		else:
			return ' '

	cv_exists.short_description = 'CV'

	def age(self):
		today = date.today()
		if self.date_of_birth is not None:
			return today.year - self.date_of_birth.year - ((self.date_of_birth.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
		else:
			return "No Age"

	def get_certs(self):
		certs = Certification.objects.filter(applicant=self)
		return certs

	get_certs.short_description = "Technical Certifications"

	class Meta:
		ordering = ['first_name']



class Certification(models.Model):
	name = models.ForeignKey(CertNames, null=True, blank=True)
	registration_number = models.CharField(max_length=100, null=True, blank=True, help_text="Cert Reg. Number (if applicable)")
	expiry_date = models.DateField(null=True, blank=True)
	valid = models.BooleanField(default=True)
	applicant = models.ForeignKey(Applicant, null=True, blank=True)

	def save(self, *args, **kwargs):
		today = date.today()
		try:
			if self.expiry_date < today:
				self.valid=False
			elif self.expiry_date == None:
				self.valid=True
		except TypeError:
			self.valid=True
		super(Certification, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name.name

	class Meta:
		verbose_name = "Technical Certification"
		verbose_name_plural = "Technical Certifications"

class GeneratedCV(models.Model):
	applicant = models.ForeignKey(Applicant, null=True, blank=True)
	latest = models.BooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.applicant.first_name + " " + self.applicant.last_name

	class Meta:
		verbose_name_plural = "Generated CVs"

class Discipline(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Professional(models.Model):
	PRO_CHOICES = (
		('Doctorate / PhD in','Doctorate PhD in'),
		('M.Phil in','M.Phil in'),
		('Master of','Master of'),
		('Bachelor of','Bachelor of'),
		('Diploma in', 'Diploma in'),
		('Certificate in','Certificate in'),
		('Vocational Training in','Vocational Training in'),
		('Other','Other'),
	)
	qualification = models.CharField(max_length=50, choices=PRO_CHOICES)
	discipline = models.ForeignKey(Discipline, null=True, blank=True)
	university = models.CharField(max_length=100, null=True, blank=True)
	year_of_completion = models.IntegerField(max_length=10, help_text='Year of Completion / Expected Completion, please input digits only e.g. "2011"', null=True, blank=True)
	applicant = models.ForeignKey(Applicant)

	def __unicode__(self):
		return str(self.qualification) + ' ' + str(self.university) + ' ' + str(self.year_of_completion)

	class Meta:
		verbose_name_plural = "Professional Qualifications"



class EmploymentHistory(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	company_name = models.CharField(max_length=100)
	project_name = models.CharField(max_length=100)
	position_held = models.CharField(max_length=100)
	responsibilities = models.TextField()
	applicant = models.ForeignKey(Applicant)

	def __unicode__(self):
		return self.project_name + " : " + str(self.start_date.year) + " - " + str(self.end_date.year)

	class Meta:
		verbose_name_plural = "Employment History"

class Contract(models.Model):
	person = models.ForeignKey(Applicant)
	project_name = models.CharField(max_length=100)







