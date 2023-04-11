from audit.models import AuditLog
from django.contrib import admin
from django.db import transaction


class AuditedModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        with transaction.atomic():
            obj.save()
            if change:
                AuditLog.objects.log(request=request, action=AuditLog.Actions.UPDATE, obj=obj)
            else:
                AuditLog.objects.log(request=request, action=AuditLog.Actions.CREATE, obj=obj)

    def delete_model(self, request, obj):
        with transaction.atomic():
            AuditLog.objects.log(request=request, action=AuditLog.Actions.DELETE, obj=obj)
            obj.delete()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            with transaction.atomic():
                AuditLog.objects.log(request=request, action=AuditLog.Actions.DELETE, obj=obj)
                obj.delete()

    def response_action(self, request, queryset):
        with transaction.atomic():
            for obj in queryset:
                AuditLog.objects.log(
                    request=request, action=AuditLog.Actions.ADMIN_ACTION,
                    description=request.POST['action'], obj=obj)
            return super().response_action(request, queryset)

    def render_change_form(self, request, context, add=False, change=False, form_url="", obj=None):
        if obj is not None:
            AuditLog.objects.log(request=request, action=AuditLog.Actions.VIEW, obj=obj)
        return super().render_change_form(request, context, add, change, form_url, obj)
