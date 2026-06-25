from django.http import (
    JsonResponse,
    HttpResponse,
)
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

import json

from .forms import ContactRequestForm

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
    IPService,
    Product,
)


def home(request):
    return render(
        request,
        "home.html",
        {
            "nav_items": NavItem.objects.all(),
            "services": Service.objects.all(),
            "benefits": Benefit.objects.all(),
            "plans": PricingPlan.objects.all(),
            "footer_links": FooterLink.objects.all(),
        },
    )


def company_dashboard(request):
    settings = SiteSettings.objects.first()

    services = ServiceCompany.objects.all()

    faqs = FAQ.objects.all()

    calculator = CalculatorSettings.objects.first()

    if request.method == "POST":
        form = ContactRequestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = ContactRequestForm()

    context = {
        "settings": settings,
        "services": services,
        "faqs": faqs,
        "calculator": calculator,
        "form": form,
    }

    return render(
        request,
        "company_dashboard.html",
        context,
    )


def ip_accounting(request):
    services = IPService.objects.all()

    return render(
        request,
        "ip_accounting.html",
        {
            "services": services,
        },
    )


# ==================================
# АНИМЕ МАГАЗИН
# ==================================

def anime_store(request):
    products = Product.objects.all()

    categories = request.GET.getlist("category")

    if categories:
        products = products.filter(
            category__in=categories
        )

    max_price = request.GET.get("max_price")

    if max_price and max_price.isdigit():
        products = products.filter(
            price__lte=int(max_price)
        )

    cart = request.session.get(
        "cart",
        {},
    )

    cart_items = []

    cart_total = 0

    for product_id, item in cart.items():

        try:
            product = Product.objects.get(
                id=int(product_id)
            )

            total_price = (
                product.price
                * item["quantity"]
            )

            cart_items.append(
                {
                    "id": product_id,
                    "name": product.name,
                    "category_display":
                        product.get_category_display(),
                    "quantity":
                        item["quantity"],
                    "price":
                        product.price,
                    "total":
                        total_price,
                }
            )

            cart_total += total_price

        except Product.DoesNotExist:

            del cart[product_id]

            request.session["cart"] = cart

    tax = int(cart_total * 0.1)

    grand_total = cart_total + tax

    context = {
        "products": products,
        "cart_items": cart_items,
        "cart_total": cart_total,
        "tax": tax,
        "grand_total": grand_total,
        "selected_categories": categories,
        "max_price": max_price or 85000,
    }

    return render(
        request,
        "anime_store.html",
        context,
    )


def add_to_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
    )

    cart = request.session.get(
        "cart",
        {},
    )

    key = str(product_id)

    if key in cart:
        cart[key]["quantity"] += 1

    else:
        cart[key] = {
            "quantity": 1
        }

    request.session["cart"] = cart

    return redirect("anime_store")


def remove_from_cart(request, product_id):
    cart = request.session.get(
        "cart",
        {},
    )

    key = str(product_id)

    if key in cart:
        del cart[key]

    request.session["cart"] = cart

    return redirect("anime_store")


def update_cart_quantity(
    request,
    product_id,
    quantity,
):
    cart = request.session.get(
        "cart",
        {},
    )

    key = str(product_id)

    if key in cart:

        if int(quantity) <= 0:
            del cart[key]

        else:
            cart[key]["quantity"] = int(
                quantity
            )

    request.session["cart"] = cart

    return redirect("anime_store")


def checkout(request):
    if request.method == "POST":

        request.session["cart"] = {}

        messages.success(
            request,
            "✅ Заказ успешно оформлен! "
            "С вами свяжется мастер для уточнения деталей.",
        )

        return redirect("anime_store")

    return redirect("anime_store")


# ==================================
# API ЗАЯВОК ИП
# ==================================

@csrf_exempt
def create_ip_request(request):

    if request.method != "POST":
        return JsonResponse(
            {
                "success": False,
                "error": "Only POST allowed",
            },
            status=405,
        )

    try:
        data = json.loads(request.body)

        request_type = data.get(
            "request_type",
            "",
        )

        name = data.get(
            "name",
            "",
        )

        phone = data.get(
            "phone",
            "",
        )

        service = data.get(
            "service",
            "",
        )

        tax_system = data.get(
            "tax_system",
            "",
        )

        price = data.get(
            "price",
            "",
        )

        message_parts = []

        if request_type:
            message_parts.append(
                f"Тип заявки: {request_type}"
            )

        if service:
            message_parts.append(
                f"Услуга: {service}"
            )

        if tax_system:
            message_parts.append(
                f"Система налогообложения: {tax_system}"
            )

        if price:
            message_parts.append(
                f"Стоимость: {price}"
            )

        ContactRequest.objects.create(
            name=name,
            phone=phone,
            message="\n".join(
                message_parts
            ),
        )

        return JsonResponse(
            {
                "success": True,
            }
        )

    except Exception as e:

        return JsonResponse(
            {
                "success": False,
                "error": str(e),
            },
            status=400,
        )
def robots_txt(request):
    return HttpResponse(
        "\n".join(
            [
                "User-agent: *",
                "Allow: /",
                "Sitemap: http://127.0.0.1:8000/sitemap.xml",
            ]
        ),
        content_type="text/plain",
    )  