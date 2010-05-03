from django.contrib import admin
from letters.models import Organization, Letter

class LetterInline(admin.TabularInline):
    extra = 3
    model = Letter


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [LetterInline]


class LetterAdmin(admin.ModelAdmin):
    search_fields = ["subject", "content"]
    list_display = ["author", "organization", "subject", "rating"]
    list_filter = ["organization"]




admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Letter, LetterAdmin)
