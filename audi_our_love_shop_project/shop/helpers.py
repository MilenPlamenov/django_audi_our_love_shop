def order_details(order, context, total, total_items_count):
    if not order.items.all():
        context['empty'] = 'Your cart is empty'
    else:
        for item in order.items.all():
            if item.product.discount_price:
                total += item.get_total_discount_product_price()
            else:
                total += item.get_total_product_price()
            total_items_count += item.quantity
        context['total'] = total
        context['total_items_count'] = total_items_count
    return total
