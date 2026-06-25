from django.contrib import admin

from .models import (
    FAQ,
    Benefit,
    CalculatorSettings,
    ContactRequest,
    FooterLink,
    NavItem,
    PricingPlan,
    Service,
    ServiceCompany,
    SiteSettings,
    IpAccountingRequest,
    IPService,
    Product,
)


admin.site.register(NavItem)
admin.site.register(Service)
admin.site.register(Benefit)
admin.site.register(PricingPlan)
admin.site.register(FooterLink)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceCompany)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
    )

    list_editable = (
        "order",
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "order",
    )

    list_editable = (
        "order",
    )


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "created_at",
        "is_processed",
    )

    list_filter = (
        "is_processed",
    )

    search_fields = (
        "name",
        "phone",
    )

    readonly_fields = (
        "created_at",
    )


@admin.register(CalculatorSettings)
class CalculatorSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(IpAccountingRequest)
class IpAccountingRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "request_type",
        "service",
        "tax_system",
        "price",
        "created_at",
        "is_processed",
    )

    list_filter = (
        "request_type",
        "is_processed",
    )

    search_fields = (
        "name",
        "phone",
    )

    readonly_fields = (
        "created_at",
    )


@admin.register(IPService)
class IPServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
        "is_highlighted",
    )

    list_editable = (
        "order",
        "is_highlighted",
    )

    ordering = (
        "order",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "name",
    )