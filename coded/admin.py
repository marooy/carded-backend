from django.contrib import admin
from .models import Profile , Follow,PhoneNumber

# Register your models here.
admin.site.register(Profile)
# admin.site.register(UserInfo)
admin.site.register(Follow)
admin.site.register(PhoneNumber)