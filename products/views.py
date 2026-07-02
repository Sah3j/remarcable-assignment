from django.shortcuts import render
from .models import Product, Category, Tag
from django.db.models import Q

"""
View for Product List page with the following funcationality:
- Search and filter
- Serches and filters preservation across searches
- Rendered via `templates/products/list.html`
"""
def product_list(request):
    products = Product.objects.all()
    q = request.GET.get("q")
    category = request.GET.get("category")
    tags = request.GET.getlist("tags")

    if q:
        products = products.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        )
    if category:
        products = products.filter(category_id=category)
    if tags:
        products = products.filter(tags__in=tags).distinct()

    return render(request, "products/list.html", {
        "products": products,
        "categories": Category.objects.all(),
        "all_tags": Tag.objects.all(),
        "search_query": q or "",
        "selected_category": category or "",
        "selected_tags": tags,
    })