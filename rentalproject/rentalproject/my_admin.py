from django.contrib import admin
from django.contrib.auth.models import User, Group

admin.site.site_header = "Texas College"
admin.site.site_title = "Texas College Admin"
admin.site.index_title = "Welcome to Texas College Admin Portal"

# admin.site.unregister(User)
# admin.site.unregister(Group)
