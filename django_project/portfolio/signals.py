from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Stock, Portfolio

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import json


# @receiver(post_save, sender=Stock)
# def create_portfolio(sender, instance, created, **kwargs):
#     if created:
#         inst = Portfolio.objects.create(stock=instance)
#         print("Created portfolio")
#         portfolio_args = Portfolio.objects.all().filter(stock=1)
#         other = getStockPrice(2, 4)
#         print(portfolio_args)
#         print(other)
#         print(inst)

@receiver(post_save, sender=Stock)
def createStockPrice(sender, instance, created, **kwargs):
    if created:
        inst = Stock.objects.all().last()
        print("doing something")
        # portfolio_args = Portfolio.objects.all().filter(stock=1)
        # other = getStockPrice(2, 4)
        # print(portfolio_args)
        # print(other)
        print(inst)
        print(type(inst))
        stock_ticker = inst.stock_ticker
        stock_created = inst.created
        var = (getStockPrice(stock_ticker))
        print("var baby ")
        var2 = (var[0][2])
        print(var2)
        print(inst.purchase_price + "hello")
        inst.purchase_price = var2
        print(inst.purchase_price)
        inst.save()
        print("added")








# @receiver(post_save, sender=Stock)
# def update_portfolio(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
#         print("updated profile")





# function => date + ticker
# return => price

def getStockPrice(num1):

    df = web.DataReader(num1, 'yahoo')
    print("result part")
    result = (df.tail(1))
    result = result.values.tolist()
    print("function type")
    print(type(result))
    return (result)


# style.use('ggplot')
#
# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2019, 11, 7)
# stock_name = 'ANF'
#
# df = web.DataReader(stock_name, 'yahoo')
# print(df.tail(6))