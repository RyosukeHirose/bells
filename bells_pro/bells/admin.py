from django.contrib import admin

from .models import Article

# admin.site.register(Article)


from mediumeditor.admin import MediumEditorAdmin

@admin.register(Article)
class MyModelAdmin(MediumEditorAdmin, admin.ModelAdmin):

    mediumeditor_fields = ('detail', )
