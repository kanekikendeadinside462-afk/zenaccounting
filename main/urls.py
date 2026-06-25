from django.urls import path

from .views import (
    home,
    company_dashboard,
    ip_accounting,
    anime_store,
    add_to_cart,
    remove_from_cart,
    update_cart_quantity,
    checkout,
    create_ip_request,
    robots_txt,
)

urlpatterns = [

    path(
        "",
        home,
        name="home",
    ),

    path(
        "company-dashboard/",
        company_dashboard,
        name="company_dashboard",
    ),

    path(
        "ip-accounting/",
        ip_accounting,
        name="ip_accounting",
    ),

    path(
        "anime-store/",
        anime_store,
        name="anime_store",
    ),

    path(
        "api/ip-request/",
        create_ip_request,
        name="create_ip_request",
    ),

    path(
        "add-to-cart/<int:product_id>/",
        add_to_cart,
        name="add_to_cart",
    ),

    path(
        "remove-from-cart/<int:product_id>/",
        remove_from_cart,
        name="remove_from_cart",
    ),

    path(
        "update-cart/<int:product_id>/<int:quantity>/",
        update_cart_quantity,
        name="update_cart_quantity",
    ),

    path(
        "checkout/",
        checkout,
        name="checkout",
    ),

    path(
        "robots.txt",
        robots_txt,
        name="robots_txt",
    ),

]