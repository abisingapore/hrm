from django.db import models
from webform.models import Applicant
from django.contrib.auth.models import User

class RequestsAndProposals(models.Model):
	date_created = models.DateField(auto_now=True)
	requested_for = models.CharField(max_length=100, verbose_name="Requestor", help_text="Company or Person making request. E.g. Total, ANOTECH etc.")
	request = models.TextField(help_text="Nature or description of request.", verbose_name="Request Description")
	duration = models.CharField(max_length=100, null=True, blank=True, help_text="Duration of Project / Request")
	poc = models.CharField(max_length=100, null=True, blank=True, verbose_name="Point of Contact", help_text="Person to liase with regarding request.")
#	to_propose = models.ManyToManyField(Applicant, null=True, blank=True, verbose_name="Candidates/Personnel to be proposed or involved.")
#	action_required = models.ManyToManyField(Action, null=True, blank=True, verbose_name="Action Required", help_text="Actions that require attention.")

	def __unicode__(self):
		return self.requested_for

	class Meta:
		ordering = ['-date_created']
		verbose_name = 'Request / Proposal Ticket'
		verbose_name_plural = 'Requests / Proposal Tickets'


class Action(models.Model):
	action = models.CharField(max_length=120)
	STATUS_CHOICES = (
		('New', 'New'),
		('Urgent', 'Urgent'),
		('Complete', 'Complete'),
		('Cancelled', 'Cancelled'),
		)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')
	request = models.ForeignKey(RequestsAndProposals)

	def __unicode__(self):
		return self.action


class Candidates(models.Model):
	request = models.ForeignKey(RequestsAndProposals)
	applicant = models.ForeignKey(Applicant)
	title_proposed = models.CharField(max_length=50, null=True, blank=True, verbose_name="Title Proposed", help_text="Job title as requested by client.")
	interview_date = models.DateField(null=True, blank=True, verbose_name="Interview Date", help_text="Known date of interview (if available).")
	STATUS_CHOICES = (
		('Proposed', 'Proposed'),
		('Accepted', 'Accepted'),
		('Rejected', 'Rejected'),
		)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Proposed')

	class Meta:
		verbose_name_plural = "Candidates"










