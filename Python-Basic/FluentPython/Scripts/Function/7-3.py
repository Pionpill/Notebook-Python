# 例7-3：register 模块
promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity_promo(order):
    '''积分 > 1000 的顾客：5% 折扣'''
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_promo(order):
    '''单个商品为 20 个或以上：10% 折扣'''
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.toal() * 0.1
    return discount

@promotion
def large_order_promo(order):
    '''订单中的不同商品达到 10 个或以上：7% 折扣'''
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0

def best_promo(order):
    '''选择可用的最佳折扣'''
    return max(promo(order) for promo in promos)