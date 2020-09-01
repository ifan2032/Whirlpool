from django.db import models

# Create your models here.
class Item(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	notes = models.CharField(max_length=300, default="N/A")


	def __str__(self):
		return f"complete: {self.title} | due date: {self.date} | notes: {self.notes}"

	def __lt__(self, other):
		return self.date < other.date