from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display

from applications.models import Application, QueueTicket


@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    list_display = ("full_name", "phone", "product", "status_badge", "created_at")
    list_filter = ("status",)
    search_fields = ("full_name", "phone")
    readonly_fields = ("full_name", "phone", "product", "note", "created_at")
    fields = ("full_name", "phone", "product", "note", "status", "created_at")

    def has_add_permission(self, request):
        return False

    @display(description="Status", label={"Yeni": "warning", "Baxılıb": "success"})
    def status_badge(self, obj):
        return obj.get_status_display()


@admin.register(QueueTicket)
class QueueTicketAdmin(ModelAdmin):
    list_display = ("code", "full_name", "branch_name", "service", "visit_date", "visit_time", "created_at")
    search_fields = ("code", "full_name", "phone", "branch_name")
    readonly_fields = ("code", "full_name", "phone", "branch_name", "service", "visit_date", "visit_time", "created_at")

    def has_add_permission(self, request):
        return False
