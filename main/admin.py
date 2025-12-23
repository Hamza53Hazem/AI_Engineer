from django.contrib import admin

from .models import ContactMessage, Service, Testimonial


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ("title", "is_active")
	list_filter = ("is_active",)
	search_fields = ("title", "description")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ("name", "role", "is_featured", "created_at")
	list_filter = ("is_featured",)
	search_fields = ("name", "role", "quote")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "created_at")
	search_fields = ("name", "email", "message")
	readonly_fields = ("created_at",)
