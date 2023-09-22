def format_currency(value):
    formatted_value = "{:,.2f}".format(value)
    formatted_currency = f"Rp. {formatted_value}"
    return formatted_currency
