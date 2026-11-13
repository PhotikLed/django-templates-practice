from django import template
from .catalog_filters import format_price, currency, price

register = template.Library()

register.filter("format_price", format_price)
register.filter("currency", currency)
register.filter("price", price)
