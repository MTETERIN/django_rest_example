from django.contrib import admin

from .models import User, Company


class CompanyModelAdmin(admin.ModelAdmin):

    class Meta:
        model = Company

admin.site.register(Company, CompanyModelAdmin)


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active']
    search_fields = ['email']
    list_editable = ['is_active']
    list_filter = ['is_active']

    class Meta:
        model = User

admin.site.register(User, UserModelAdmin)
