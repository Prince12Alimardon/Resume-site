from django.contrib import admin
from .models import About, Partner, Resume, AdditionalInfo, Project
from django.db import models
from django.forms import Textarea


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth', 'zip_code')


class AdditionalInfoInline(admin.StackedInline):
    model = AdditionalInfo
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 40})},
    }

    fieldsets = (
        (None, {
            'fields': (('start_finish', 'profession', 'academy'), ('icon', 'content'))
        }),
        ('Skill info', {
            'fields': (('title', 'percent', 'is_main'),)
        }),
    )
    extra = 0


class ResumeAdmin(admin.ModelAdmin):
    inlines = [AdditionalInfoInline]
    list_display = ('id', 'type', 'is_skill')
    list_filter = ('is_skill',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession')
    filter_horizontal = ('category',)


admin.site.register(About, AboutAdmin)
admin.site.register(Partner)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Project, ProjectAdmin)
