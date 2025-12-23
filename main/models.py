from django.db import models


class Service(models.Model):
	"""Services offered on the marketing site."""

	title = models.CharField(max_length=100)
	description = models.TextField()
	icon = models.CharField(max_length=50, blank=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ["title"]

	def __str__(self) -> str:
		return self.title


class Testimonial(models.Model):
	"""Short quotes from customers."""

	name = models.CharField(max_length=80)
	role = models.CharField(max_length=80, blank=True)
	quote = models.TextField()
	is_featured = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return f"{self.name} ({self.role})" if self.role else self.name


class ContactMessage(models.Model):
	"""Stores messages submitted from the contact form."""

	name = models.CharField(max_length=8)
	email = models.EmailField()
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return f"Message from {self.name}"
