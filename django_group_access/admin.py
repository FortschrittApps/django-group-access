from django.contrib import admin
from django_group_access.models import *


class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('members',)

admin.site.register(AccessGroup, GroupAdmin)
admin.site.register(Invitation)