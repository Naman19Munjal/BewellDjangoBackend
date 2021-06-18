from django.contrib import admin
from .models import Post,Volunteer,MedicineDonation,PostComment,Doctor,Session
# Register your models here.

admin.site.register((Post,PostComment))
admin.site.register(Volunteer)
admin.site.register(MedicineDonation)
admin.site.register(Doctor)
admin.site.register(Session)