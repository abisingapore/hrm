from django.contrib import admin
from dash.models import *
from django.utils.safestring import mark_safe
from django.utils.text import capfirst

class ActionInline(admin.TabularInline):
	model=Action
	extra=1

class CandidateInline(admin.TabularInline):
	model=Candidates
	extra=1

class RequestAdmin(admin.ModelAdmin):
	inlines = [ActionInline, CandidateInline,]
	list_display = ['date_created', 'requested_for', 'request', 'duration', 'poc', 'proposed', 'accepted', 'rejected', 'follow_up',]
	list_filter = ['date_created',]
	search_fields = ['requested_for', 'request', 'duration', 'poc', 'follow_up']

	def proposed(self, obj):
		br = mark_safe('<br>')
		candidates = obj.candidates_set.all()
		candidatelist = []
		for c in candidates:
			candidatelist.append(mark_safe('<a href = "/admin/webform/applicant/%s" target="_blank">%s</a>') % (c.applicant.id, c.applicant.full_name()))
		html = mark_safe(br.join([c for c in candidatelist]))
		return html

	def accepted(self, obj):
		br = mark_safe('<br>')
		candidates = obj.candidates_set.filter(status='Accepted')
		candidatelist = []
		for c in candidates:
			candidatelist.append(mark_safe('<a href = "/admin/webform/applicant/%s" target="_blank">%s</a>') % (c.applicant.id, c.applicant.full_name()))
		html = mark_safe(br.join([c for c in candidatelist]))
		return html

	def rejected(self, obj):
		br = mark_safe('<br>')
		candidates = obj.candidates_set.filter(status='Rejected')
		candidatelist = []
		for c in candidates:
			candidatelist.append(mark_safe('<a href = "/admin/webform/applicant/%s" target="_blank">%s</a>') % (c.applicant.id, c.applicant.full_name()))
		html = mark_safe(br.join([c for c in candidatelist]))
		return html

	proposed.short_description = "Candidates to Propose"

	def follow_up(self, obj):
		actions = Action.objects.filter(request=obj)
		br = mark_safe('<br>')
		actionlist = [] 
		for a in actions:
			if a.status == 'Complete':
				actionlist.append(mark_safe('<span style="color:#5cb85c; text-decoration: line-through;">%s</span>') % capfirst(a.action))
			elif a.status == 'Urgent':
				actionlist.append(mark_safe('<div style="padding:2px; border:2px solid #d9534f;"><span style="color:#d9534f;">!! %s</span></div>') % capfirst(a.action))
			elif a.status == 'New':
				actionlist.append(mark_safe('<div style="padding:2px; border:2px solid #f0ad4e;"><span style="color:#f0ad4e;"> %s</span></div>') % capfirst(a.action))
			elif a.status == 'Cancelled':
				actionlist.append(mark_safe('<span style="text-decoration: line-through;">%s</span>') % capfirst(a.action))				

		html = mark_safe(br.join([p for p in actionlist]))
		return html

	follow_up.short_description = "Action Follow Up"

admin.site.register(Action)
admin.site.register(RequestsAndProposals, RequestAdmin)
admin.site.register(Candidates)