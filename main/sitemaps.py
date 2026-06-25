from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            "home",
            "company_dashboard",
            "ip_accounting",
            "anime_store",
        ]

    def location(self, item):
        return reverse(item)