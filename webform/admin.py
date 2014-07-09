from django.contrib import admin
from myproject import settings
from webform.models import Applicant, Specialization, GeneratedCV, Certification, EmploymentHistory, GeneratedCV, Contract, Professional, CertNames, Discipline
from django import forms
import os
from webform.forms import *
from django.conf.urls import patterns, include, url
from django.db import models
from django.forms.extras.widgets import SelectDateWidget
from django.forms import extras, widgets, TextInput, Textarea
from datetime import date
from django.http import HttpResponseRedirect
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from time import sleep
from django.utils.safestring import mark_safe
#from django.contrib.admin import site
#import adminactions.actions as actions
import datetime
import re

from django.forms.widgets import Widget, Select
from django.utils.dates import MONTHS
from django.utils.safestring import mark_safe


__all__ = ('MonthYearWidget',)

RE_DATE = re.compile(r'(\d{4})-(\d\d?)-(\d\d?)$')

class MonthYearWidget(Widget):
    """
    A Widget that splits date input into two <select> boxes for month and year,
    with 'day' defaulting to the first of the month.

    Based on SelectDateWidget, in 

    django/trunk/django/forms/extras/widgets.py


    """
    none_value = (0, '---')
    month_field = '%s_month'
    year_field = '%s_year'

    def __init__(self, attrs=None, years=None, required=True):
        # years is an optional list/tuple of years to use in the "year" select box.
        self.attrs = attrs or {}
        self.required = required
        if years:
            self.years = years
        else:
            this_year = datetime.date.today().year -64
            self.years = range(this_year, this_year+65)

    def render(self, name, value, attrs=None):
        try:
            year_val, month_val = value.year, value.month
        except AttributeError:
            year_val = month_val = None
            if isinstance(value, basestring):
                match = RE_DATE.match(value)
                if match:
                    year_val, month_val, day_val = [int(v) for v in match.groups()]

        output = []

        if 'id' in self.attrs:
            id_ = self.attrs['id']
        else:
            id_ = 'id_%s' % name

        month_choices = MONTHS.items()
        if not (self.required and value):
            month_choices.append(self.none_value)
        month_choices.sort()
        local_attrs = self.build_attrs(id=self.month_field % id_)
        s = Select(choices=month_choices)
        select_html = s.render(self.month_field % name, month_val, local_attrs)
        output.append(select_html)

        year_choices = [(i, i) for i in self.years]
        if not (self.required and value):
            year_choices.insert(0, self.none_value)
        local_attrs['id'] = self.year_field % id_
        s = Select(choices=year_choices)
        select_html = s.render(self.year_field % name, year_val, local_attrs)
        output.append(select_html)

        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_):
        return '%s_month' % id_
    id_for_label = classmethod(id_for_label)

    def value_from_datadict(self, data, files, name):
        y = data.get(self.year_field % name)
        m = data.get(self.month_field % name)
        if y == m == "0":
            return None
        if y and m:
            return '%s-%s-%s' % (y, m, 1)
        return data.get(name, None)

class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        months= (
        	('January', 'January'),
        	('February', 'February'),
        	('March', 'March'),
        	('April', 'April'),
        	('May', 'May'),
        	('June', 'June'),
        	('July', 'July'),
        	('August', 'August'),
        	('September', 'September'),
        	('October', 'October'),
        	('November', 'November'),
        	('December', 'December'),
        	)
        _widgets = (
            widgets.Select(attrs=attrs, choices=((str(x), x) for x in range(1,31))),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=((str(x), x) for x in range(1930,2015))),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return u''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(day=int(datelist[0]), month=int(datelist[1]),
                    year=int(datelist[2]))
        except ValueError:
            return ''
        else:
            return str(D)

class EmploymentInline(admin.TabularInline):
	model=EmploymentHistory
	extra=1
	formfield_overrides = {
		models.DateField: {'widget': MonthYearWidget(attrs={'size':'0'})},
		models.CharField: {'widget': TextInput(attrs={'size':'0'})},
	}
	classes = ('grp-collapse grp-closed',)
	inline_classes = ('grp-collapse grp-closed',)

class EmploymentHistoryAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.DateField: {'widget': MonthYearWidget},
	}

class ProfessionalInline(admin.TabularInline):
	model = Professional
	extra = 1
	classes = ('grp-collapse grp-closed',)
	inline_classes = ('grp-collapse grp-closed',)

class CertificationInline(admin.TabularInline):
	model=Certification
	extra=1
	classes = ('grp-collapse grp-closed',)
	inline_classes = ('grp-collapse grp-closed',)




class HelloPDFView(PDFTemplateView, PDFTemplateResponseMixin):
	template_name = "hello.html"
	def get_cv():
		try:
			cv = GeneratedCV.objects.get(latest=True)
		except GeneratedCV.DoesNotExist:
			cv = None
		return cv

	pdf_filename = str(get_cv().applicant.first_name) + " " + str(get_cv().applicant.last_name) + ".pdf"


	def get_context_data(self, **kwargs):
		cv = GeneratedCV.objects.get(latest=True)
		self.pdf_filename = str(cv.applicant.first_name) + str(cv.applicant.last_name) + ".pdf"
		certification = cv.applicant.certification_set.all()
		qualification = cv.applicant.professional_set.all()
		history = cv.applicant.employmenthistory_set.all().order_by('-start_date')
		try:
			first = history[0]
		except IndexError:
			first = None
		specialization = "\n | ".join([p.name for p in cv.applicant.spec_summary.all()])
	    	return super(HelloPDFView, self).get_context_data(pagesize="A4", 
	    		applicant=cv.applicant,
	    		specialization=specialization,
	    		qualification=qualification,
	    		certification=certification,
	    		history=history,
	    		first=first,
	    		**kwargs)



def generate_cv(modeladmin, request, queryset):
	item = queryset.get()
	GeneratedCV.objects.all().delete()
	GeneratedCV.objects.create(applicant=item, latest=True)
	return HttpResponseRedirect('/generate.pdf')



generate_cv.short_description = "Generate CV from selected"

class ApplicantAdmin(admin.ModelAdmin):
	search_fields = ['first_name', 'last_name', 'spec_summary__name',]
	list_filter = ('spec_summary', 'blacklist',)
	list_display = ('first_name', 'last_name', 'age', 'nationality', 'specialization', 'certification', 'email', 'cv_exists' )
	filter_horizontal = ('spec_summary',)
#	change_list_template = "admin/change_list_filter_sidebar.html"
#	change_list_filter_template = "admin/filter_listing.html"
	actions = [generate_cv]
	exclude = ('confirm_email',)
	fieldsets = (
		('Personal Information', {
			'classes':('grp-collapse grp-closed',),
			'fields' : (('first_name',
						'last_name'),
						('known_as',
						'date_of_birth'),
						'nationality',  
						('add_nationality',
						'add_nat_status'),
						('gender',
						'marital_status'), 
				)

			}),
		('Contact Information', {
			'classes':('grp-collapse grp-closed',),
			'fields' : ('email',
						('contact_home',
						'contact_mobile'),
						'address_line_1',
						'address_line_2',
						('city',
						'state'),
						('postal_code',
						'country'),
				)
			}),
		('Professional Information', {
			'classes':('grp-collapse grp-closed',),
			'fields' : ('abi_summary',
						'spec_summary',
						'proposed_specialization',
						'language_proficiency',
						'computer_literacy',
						('current_salary',
						'notice_period'),
						('current_pos',
						'whereabouts'),
						'describe_self',
				)

			}),

		("Professional Qualification", {"classes": ('grp-collapse grp-closed', 'placeholder professional_set-group', ), "fields" : ()}),
		("Technical Certification", {"classes": ('grp-collapse grp-closed', 'placeholder certification_set-group',), "fields" : ()}),
		("Employment History", {"classes": ('grp-collapse grp-closed', 'placeholder employmenthistory_set-group', ), "fields" : ()}),


		('Curriculum Vitae', {
			'classes':('grp-collapse grp-closed',),
			'fields' : ('cv',
				)
			}),

		('Declaration and Terms of Service', {
			'classes':('grp-collapse grp-closed',),
			'fields' : ('declaration',
						'tos',
						'blacklist',
						'blacklist_reason',
				)
			})

	)
	inlines = [ EmploymentInline, ProfessionalInline, CertificationInline,
	]



	def specialization(self, obj):
		br = mark_safe('<br>')
		html = mark_safe(br.join([p.name for p in obj.spec_summary.all()]))
		return html

	def certification(self, obj):
		br = mark_safe('<br>')
		certs = obj.get_certs()
		html = mark_safe(br.join([c.name.name for c in certs]))
		return html

class ApplicantForm(forms.ModelForm):
	class Meta:
		model = Applicant

	def clean(self):
		cleaned_date = self.cleaned_data
		email = cleaned_data.get('email')
		try:
			Applicant.objects.get(email__iexact=email)
		except Applicant.DoesNotExist:
			return cleaned_data
		raise forms.ValidationError(u'That email address is already in use. Please use another.')

class SpecializationForm(forms.ModelForm):
	class Meta:
		model = Specialization

	def clean(self):
		cleaned_data = self.cleaned_data
		name = cleaned_data.get('name')
		try:
			Specialization.objects.get(name__iexact=name)
		except Specialization.DoesNotExist:
			return cleaned_data
		raise forms.ValidationError(u'That Specialization Already Exists!')

class GeneratedCVAdmin(admin.ModelAdmin):
	list_display = ('applicant', 'latest', 'date_created',)	

class SpecializationAdmin(admin.ModelAdmin):
	search_fields = ['name',]
	form = SpecializationForm

class CertificationAdmin(admin.ModelAdmin):
	search_fields = ['name',]

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Contract)
admin.site.register(EmploymentHistory, EmploymentHistoryAdmin)
admin.site.register(CertNames)
admin.site.register(Discipline)
#actions.add_to_site(site)
