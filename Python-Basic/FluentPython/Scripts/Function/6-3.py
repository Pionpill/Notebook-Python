# 例6-3：Order 类和使用函数实现的折扣策略
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    '''购买商品类'''

    def __init__(self, product, quantity, price):
        '''构造方法
        :param product:商品
        :param quantity:商品数量
        :param price:商品价格
        '''
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        '''
        :return:商品总价
        '''
        return self.price * self.quantity


class Order:
    '''订购类'''

    def __init__(self, customer: Customer, cart: LineItem, promotion=None):
        '''构造方法
        :param customer:用户
        :param cart:购物车
        :param promotion:打折方式(函数)
        '''
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        '''计算购物车中商品总价'''
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        '''最终价格：总价 - 折扣价'''
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        '''格式化输出'''
        fmt = '<Order total:{:.2f} dur:{:.2f}>'
        return fmt.format(self.total(), self.due())
    
def fidelity_promo(order):
    '''积分 > 1000 的顾客：5% 折扣'''
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

def bulk_promo(order):
    '''单个商品为 20 个或以上：10% 折扣'''
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.toal() * 0.1
    return discount

def large_order_promo(order):
    '''订单中的不同商品达到 10 个或以上：7% 折扣'''
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0