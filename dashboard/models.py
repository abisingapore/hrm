from django.db import models
from django.contrib.auth.models import User

class ToDoLists(models.Model):
	date = models.DateField(auto_now_add=True)
	creator = models.ForeignKey(User)
	notes = models.TextField(null=True, blank=True, help_text="(optional)", verbose_name='Instructions')





