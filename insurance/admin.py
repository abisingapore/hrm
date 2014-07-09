from django.contrib import admin
from insurance.models import Job, Worker, ContractYear, Provider, Report, ReportDetails
import json
from django.db import models
import HTMLParser
from django.forms.extras.widgets import SelectDateWidget
from django.forms import TextInput, Textarea
from easy_pdf.views import PDFTemplateView
from django.http import HttpResponseRedirect

def get_report():
	try:
		report = Report.objects.filter(latest=True).get()
	except Report.DoesNotExist:
		report = None
	return report

class HelloPDFViewInsurance(PDFTemplateView):
	report = get_report()
	template_name = "insurance_report.html"
	pdf_filename = str(report) + ".pdf"
	def get_context_data(self, **kwargs):
	    	return super(HelloPDFViewInsurance, self).get_context_data(
	    		pagesize="A4", 
	    		first_name=get_report(),
	    		reports = ReportDetails.objects.all(),
	    		latest_report=Report.objects.filter(latest=True).get(),
	    		**kwargs)

def generate_report(modeladmin, request, queryset):
	Report.objects.all().update(latest=False)
	ReportDetails.objects.all().delete()
	new_report = Report.objects.create(total_cost=0.0, latest=True)
	total_cost = []
	for q in queryset:
		full_name = q.worker
		total_days_worked = q.total_days()
		display_cost = q.get_rate()
		project_name = q.project_name
		start_date = q.start_date
		end_date = q.end_date
		job_cost = q.job_cost_nostring()
		year = q.year
		provider = q.get_provider()
		total_cost.append(q.job_cost_nostring())
		ReportDetails.objects.create(
			report=new_report, 
			full_name=full_name,
			total_days_worked=total_days_worked,
			display_cost=display_cost,
			project_name=project_name,
			start_date=start_date,
			end_date=end_date,
			job_cost=job_cost,
			year=year,
			provider=provider,
			)
	total_cost = round(sum(total_cost), 2)
	new_report.total_cost = total_cost
	new_report.save()
	return HttpResponseRedirect('/generate_insurance.pdf')


class JobAdmin(admin.ModelAdmin):
	list_display = ['worker', 'project_name', 'get_rate', 'start_date', 'end_date', 'total_days', 'job_cost', 'year', 'get_provider']
	list_filter = ['year', 'year__provider',]
	change_list_template = "admin/change_list_filter_sidebar.html"
	change_list_filter_template = "admin/filter_listing.html"
	formfield_overrides = {
		models.DateField: {'widget': SelectDateWidget(years=range(2010, 2017))}
	}
	search_fields = ['worker__first_name', 'worker__last_name', 'project_name']
	actions = [generate_report]
	list_per_page = 50


class JobInline(admin.TabularInline):
	model=Job
	extra=0
	formfield_overrides = {
		models.DateField: {'widget': SelectDateWidget(years=range(2010, 2017))},
		models.CharField:{'widget': TextInput(attrs={'size':'20'})}
	}


class WorkerAdmin(admin.ModelAdmin):
	list_display = ['get_full_name', 'first_name', 'last_name', 'total_days_worked', 'total_weeks_worked', 'display_cost', 'project_history', ]
	search_fields = ['first_name', 'last_name']
	inlines = [JobInline]

	def project_history(self, obj):
		jobs = Job.objects.filter(worker=obj)
		project_history = []
		for job in jobs:
			period = job.end_date - job.start_date
			period = int(period.days) + 1
			description = job.project_name + ' - ' + str(job.start_date.strftime('%d %b %Y')) + ' to ' + str(job.end_date.strftime('%d %b %Y')) + ' (' + str(period) + ' days)' 
			project_history.append(description)
		h = HTMLParser.HTMLParser()
		return (h.unescape("\n | ".join(project_history)))

class ContractYearAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'provider']
	formfield_overrides = {
		models.DateField: {'widget': SelectDateWidget(years=range(2010, 2017))}
	}

class ReportAdmin(admin.ModelAdmin):
	list_display = ['date', 'display_cost', 'latest']


admin.site.register(Job, JobAdmin)
admin.site.register(ContractYear, ContractYearAdmin)
admin.site.register(Provider)
admin.site.register(Report, ReportAdmin)


