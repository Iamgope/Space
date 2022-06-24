from django.contrib import admin

# Register your models here.
from .models import Posts, space,subscription,Comment
admin.site.register(space)
admin.site.register(subscription)
admin.site.register(Posts)
admin.site.register(Comment)