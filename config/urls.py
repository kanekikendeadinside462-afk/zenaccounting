from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap
from django.conf import settings

sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    path("", include("main.urls")),
]