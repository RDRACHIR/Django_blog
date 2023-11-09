from django.contrib import admin

# Models
from .models import Project

# Register your models here.
# admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id','title','created' )
  list_display_links = ('id','title')
  list_filter = ('title','created','update')
  search_fields = ('title', 'desc')
  
  readonly_fields=('created','update')