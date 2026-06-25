from django.db import models


class NavItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Benefit(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_popular = models.BooleanField(default=False)

    companies_limit = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)

    bank_integration = models.BooleanField(default=False)
    analytics = models.BooleanField(default=False)
    merch = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FooterLink(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category} - {self.title}"


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default="ZenAccounting")

    hero_title = models.CharField(max_length=255)
    hero_title_colored = models.CharField(max_length=255)

    hero_description = models.TextField()

    security_title = models.CharField(max_length=255)
    security_description = models.CharField(max_length=255)

    experience_years = models.PositiveIntegerField(default=15)

    phone = models.CharField(max_length=50)
    email = models.EmailField()

    address = models.TextField()

    footer_text = models.TextField()

    privacy_policy_url = models.URLField(blank=True)
    offer_url = models.URLField(blank=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"


class ServiceCompany(models.Model):
    ICON_CHOICES = [
        ("account_balance_wallet", "Бухгалтерия"),
        ("badge", "Кадры"),
        ("query_stats", "Аудит"),
        ("gavel", "Юридические услуги"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100, choices=ICON_CHOICES)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"


class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class CalculatorSettings(models.Model):
    usn_base_price = models.PositiveIntegerField(default=5000)
    osno_base_price = models.PositiveIntegerField(default=12000)

    employee_price = models.PositiveIntegerField(default=700)

    max_employees = models.PositiveIntegerField(default=50)

    def __str__(self):
        return "Настройки калькулятора"

    class Meta:
        verbose_name = "Калькулятор"
        verbose_name_plural = "Калькулятор"

class IpAccountingRequest(models.Model):
    REQUEST_TYPES = [
        ("consultation", "Консультация"),
        ("calculator", "Калькулятор"),
    ]

    request_type = models.CharField(
        max_length=50,
        choices=REQUEST_TYPES,
    )

    service = models.CharField(
        max_length=255,
        blank=True,
    )

    name = models.CharField(
        max_length=255,
    )

    phone = models.CharField(
        max_length=50,
    )

    tax_system = models.CharField(
        max_length=255,
        blank=True,
    )

    price = models.CharField(
        max_length=100,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_processed = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка ИП"
        verbose_name_plural = "Заявки ИП"

class IPService(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    is_highlighted = models.BooleanField(
        default=False,
        verbose_name="Красная карточка"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Услуга ИП"
        verbose_name_plural = "Услуги ИП"

    def __str__(self):
        return self.title


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("resin", "Смоляные фигурки"),
        ("clay", "Полимерная глина"),
        ("doll", "Арт-куклы"),
        ("diorama", "Миниатюры"),
    ]

    name = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
    )

    price = models.IntegerField(
        help_text="Цена в йенах"
    )

    image_url = models.URLField(
        blank=True,
        default=""
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"