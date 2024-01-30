from django.contrib import admin
from .models import Location, Category, Tour, Review, Booking, Comment, Payment

# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(Comment)
admin.site.register(Payment)

