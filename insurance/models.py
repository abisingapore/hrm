from django.db import models
import HTMLParser

class Worker(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	def total_days_worked(self):
		jobs = Job.objects.filter(worker=self)
		days = []
		n=0
		for job in jobs:
			dt = (job.end_date - job.start_date).days
			days.append(int(dt))
			n=jobs.count()
		return sum(days, n)

	def total_weeks_worked(self):
		return round(float(self.total_days_worked() / 7.0), 1) 

	def total_cost(self):
		jobs = Job.objects.filter(worker=self)
		costs = []
		for job in jobs:
			a = job.rate * (self.total_days_worked() / 365.0)
			a = a / jobs.count()
			costs.append(a)
		cost = round(sum(costs), 2)
		return cost

	def display_cost(self):
		return "$ " + str(self.total_cost())
	display_cost.short_description = "Overseas Secondment Cost (Prorated)"

	def get_years(self):
		years = self.job.year
		return years

	def project_history(self):
		jobs = Job.objects.filter(worker=self)
		project_history = []
		for job in jobs:
			period = job.end_date - job.start_date
			period = int(period.days) + 1
			description = job.project_name + ' - ' + str(job.start_date.strftime('%d %b %Y')) + ' to ' + str(job.end_date.strftime('%d %b %Y')) + ' (' + str(period) + ' days)' 
			project_history.append(description)
		h = HTMLParser.HTMLParser()
		return (h.unescape("\n | ".join(project_history)))


	def get_full_name(self):
		return self.first_name + " " + self.last_name

	get_full_name.short_description = "Full Name"

	class Meta:
		ordering = ['-date_created',]
		verbose_name = "Insured Staff"
		verbose_name_plural = "Insured Staff"

class Provider(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "Insurer"
		verbose_name_plural = "Insurers"


class ContractYear(models.Model):
	provider = models.ForeignKey(Provider)
	year_start = models.DateField(auto_now=False)
	year_end = models.DateField(auto_now=False)

	def __unicode__(self):
		return str(self.year_start.strftime('%d')) + " " + str(self.year_start.strftime('%b')) + " " + str(self.year_start.year) + " - " + str(self.year_end.strftime('%d')) + " " + str(self.year_end.strftime('%b')) + " " + str(self.year_end.year) 


	class Meta:
		verbose_name = "Year"
		verbose_name_plural = "Years"



class Job(models.Model):
	worker = models.ForeignKey(Worker)
	year = models.ForeignKey(ContractYear, help_text="Period of policy")
	project_name = models.CharField(max_length=30, help_text="Name of project e.g. (TEPM)")
	rate = models.FloatField(default="860.0", help_text="Rate per annum $SGD")
	start_date = models.DateField(help_text="Date of Mobilization")
	end_date = models.DateField(help_text="Date of De-Mobilization")

	def __unicode__(self):
		return self.project_name + " " + str(self.start_date) + " " + str(self.end_date)

	def total_days(self):
		dt = self.end_date - self.start_date	
		return dt.days + 1

	def get_provider(self):
		return self.year.provider.name

	def get_rate(self):
		return "$ " + str(self.rate) + " / year"

	def job_cost(self):
		cost = self.rate * (self.total_days() / 365.0)
		cost = round(cost, 2)
		return "$ " + str(cost)

	def job_cost_nostring(self):
		cost = self.rate * (self.total_days() / 365.0)
		cost = round(cost, 2)
		return cost

	job_cost.short_description = "Cost of policy (Prorated)"
	get_provider.short_description = "Insurance Provider"
	get_rate.short_description = "Rate per annum"

	class Meta:
		verbose_name = "Policy"
		verbose_name_plural = "Policies"

class Report(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	total_cost = models.CharField(max_length=50)
	latest = models.BooleanField(default=True)

	def __unicode__(self):
		return "Report Generated: " + str(self.date.strftime('%d %b %Y'))

	def display_cost(self):
		return "$ " + str(self.total_cost)

	class Meta:
		verbose_name = "Recent Report"
		verbose_name_plural = "Recent Reports"
	display_cost.short_description = "Total Cost"

class ReportDetails(models.Model):
	report = models.ForeignKey(Report)
	full_name = models.CharField(max_length=100)
	total_days_worked = models.CharField(max_length=10)
	display_cost = models.CharField(max_length=20)
	project_name = models.CharField(max_length=30)
	start_date = models.DateField()
	end_date = models.DateField()
	job_cost = models.CharField(max_length=20)
	year = models.CharField(max_length=20)
	provider = models.CharField(max_length=50)

	def __unicode__(self):
		return self.full_name + " : " + self.project_name + " - " + self.start_date.strftime('%d %b %Y') + " to " + self.end_date.strftime('%d %b %Y')

'''
		full_name = q.worker
		total_days_worked = q.total_days()
		display_cost = q.get_rate()
		project_name = q.project_name
		start_date = q.start_date
		end_date = q.end_date
		year = q.year
		provider = q.get_provider()
'''



