from django import template

register = template.Library()


@register.filter(name="format_price")
def format_price(value, currency="руб."):
    if value is None or value == "":
        return ""
    return f"{value} {currency}"


@register.filter(name="currency")
def currency(value, currency="руб."):
    return format_price(value, currency)


@register.filter(name="price")
def price(value, currency="руб."):
    return format_price(value, currency)
