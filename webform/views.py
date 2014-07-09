from django.shortcuts import render
from webform.models import Applicant
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from django import forms
from django.forms import extras
from django_countries import countries
import json


def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def signup(request):
	class ApplicantForm(ModelForm):
		class Meta:
			model = Applicant
			fields = ['first_name', 
						'last_name', 
						'nationality', 
						'date_of_birth', 
						'email',
						'confirm_email', 
						'contact_home',
						'contact_mobile',
						'marital_status',
						'gender',
						'address_line_1',
						'address_line_2',
						'city',
						'state',
						'postal_code',
						'country',
						'qualification',
						'spec_summary',
						'technical',
						'current_salary',
						'notice_period',
						'current_pos',
						'whereabouts',
						'offshore',
						'onshore_singapore',
						'onshore_asiapac',
						'onshore_mideast',
						'onshore_africa',
						'onshore_europeusa',
						'offshore_singapore',
						'offshore_asiapac',
						'offshore_mideast',
						'offshore_africa',
						'offshore_europeusa',
						'preferred_places',
						'describe_self',
						'employment_history',
						'cv',
						'declaration',
						'tos',
						]
		def clean_preferred_places(self):
			preferred_places = self.cleaned_data.get('preferred_places', None)
			preferred_list = (", ".join(preferred_places))
			return preferred_list

		def clean(self):
			email = self.cleaned_data.get('email', None)
			cemail = self.cleaned_data.get('confirm_email', None)
			if email and cemail and (email == cemail):
				return self.cleaned_data
			else:
				raise forms.ValidationError("The email addresses did not match. Please try again.")
		date_of_birth = forms.DateField(widget=extras.SelectDateWidget)
		OPTIONS = (
			('Singapore', 'Singapore'),
			('Asia Pacific', 'Asia Pacific'),
			('Middle East', 'Middle East'),
			('Africa', 'Africa'),
			('Europe and USA', 'Europe and USA')
		)

		preferred_places = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)


	form = ApplicantForm()
	years = []
	for x in range(1929,2000):
		years.append(x)
	years = reversed(years)
	if request.method == 'POST':
		form = ApplicantForm(request.POST)
		if form.is_valid():
			applicant=Applicant(first_name=form.cleaned_data['first_name'],
				last_name=form.cleaned_data['last_name'],
				nationality=form.cleaned_data['nationality'],
				date_of_birth=form.cleaned_data['date_of_birth'],
				email=form.cleaned_data['email'],
				contact_home=form.cleaned_data['contact_home'],
				contact_mobile=form.cleaned_data['contact_mobile'],
				marital_status=form.cleaned_data['marital_status'],
				gender=form.cleaned_data['gender'],
				address_line_1=form.cleaned_data['address_line_1'],
				address_line_2=form.cleaned_data['address_line_2'],
				city=form.cleaned_data['city'],
				state=form.cleaned_data['state'],
				postal_code=form.cleaned_data['postal_code'],
				country=form.cleaned_data['country'],
				qualification=form.cleaned_data['qualification'],
				spec_summary=form.cleaned_data['spec_summary'],
				technical=form.cleaned_data['technical'],
				current_salary=form.cleaned_data['current_salary'],
				notice_period=form.cleaned_data['notice_period'],
				current_pos=form.cleaned_data['current_pos'],
				whereabouts=form.cleaned_data['whereabouts'],
				offshore=form.cleaned_data['offshore'],
				onshore_singapore=form.cleaned_data['onshore_singapore'],
				onshore_asiapac=form.cleaned_data['onshore_asiapac'],
				onshore_mideast=form.cleaned_data['onshore_mideast'],
				onshore_africa=form.cleaned_data['onshore_africa'],
				onshore_europeusa=form.cleaned_data['onshore_europeusa'],
				offshore_singapore=form.cleaned_data['offshore_singapore'],
				offshore_asiapac=form.cleaned_data['offshore_asiapac'],
				offshore_mideast=form.cleaned_data['offshore_mideast'],
				offshore_africa=form.cleaned_data['offshore_africa'],
				offshore_europeusa=form.cleaned_data['offshore_europeusa'],
				preferred_places=form.cleaned_data['preferred_places'],
				describe_self=form.cleaned_data['describe_self'],
				employment_history=form.cleaned_data['employment_history'],
				cv=form.cleaned_data['cv'],
				declaration=form.cleaned_data['declaration'],
				tos=form.cleaned_data['tos'],
				)
			applicant.save()
			return HttpResponseRedirect('/')
	return render_to_response('signup.html', {'form':form, 'years':years}, context_instance=RequestContext(request))



















