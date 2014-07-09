from django.shortcuts import render
from webform.models import Applicant
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from django import forms
from django.forms import extras
from django_countries import countries
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import AuthenticationForm

class ReCaptchaLoginForm(AuthenticationForm):
	catpcha = ReCaptchaField(attrs={'theme':'clean'})










