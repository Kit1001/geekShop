import datetime
import os
import json

from django.shortcuts import render


def main(request):
    title = "главная"

    with open(os.path.join('jsons', 'products.json'), 'r', encoding='UTF-8') as f:
        products = json.load(f)

    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"

    with open(os.path.join('jsons', 'links_menu.json'), 'r', encoding='UTF-8') as f:
        links_menu = json.load(f)

    with open(os.path.join('jsons', 'same_products.json'), 'r', encoding='UTF-8') as f:
        same_products = json.load(f)

    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()

    with open(os.path.join('jsons', 'locations.json'), 'r', encoding='UTF-8') as f:
        locations = json.load(f)

    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
