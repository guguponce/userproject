from django.contrib import admin
from users.models import Usuarios,Comments,UserProfileData
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Comments)
admin.site.register(UserProfileData)
