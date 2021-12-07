# 例6-1：实现 Order 类，支持插入式折扣策略
from abc import ABC, abstractclassmethod, abstractmethod
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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        '''格式化输出'''
        fmt = '<Order total:{:.2f} dur:{:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣金额(正值)"""


class FidelityPromo(Promotion):
    """积分 > 1000 客户，提供 5% 折扣"""
    
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """单个商品为 20 或以上，提供 10% 折扣"""
    
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """订单中不同商品达到 10 个或以上，提供 7% 折扣"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
    
    
joe = Customer('John Doe',0)
ann = Customer('Ann Smith',1100)
cart = [LineItem('banana',4,.5),
        LineItem('apple',10,1.5),
        LineItem('watermelon',5,5.0)]
print(Order(joe,cart,FidelityPromo()))  # <Order total:42.00 dur:42.00>
print(Order(ann,cart,FidelityPromo()))  # <Order total:42.00 dur:39.90>

banana_cart = [LineItem('banana',30,.5),
               LineItem('apple',10,1.5)]
print(Order(joe,banana_cart,BulkItemPromo()))   # <Order total:30.00 dur:28.50>

long_order = [LineItem(str(item_code),1,1.0)
              for item_code in range(10)]
print(Order(joe,long_order,LargeOrderPromo()))  # <Order total:10.00 dur:9.30>