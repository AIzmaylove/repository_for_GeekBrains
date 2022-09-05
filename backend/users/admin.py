from django.contrib import admin
from users import models
#from .models import CustomUser
from django.contrib.auth.admin import UserAdmin



# admin.site.register(CustomUser)

@admin.register(models.CustomUser)
class CustomUserModelAdmin(UserAdmin):
    pass
    # list_display = ["id", "username", "email", "is_active", "date_joined"]
    # ordering = ["-date_joined"]