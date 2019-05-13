#coding:utf-8
import ConfigParser
import tushare

class Stock():
    def __init__(self,stock_num):
        self.stock_num = stock_num
    def get_price(self):
        current_price = tushare.get_realtime_quotes(self.stock_num)['open'][0]
        return current_price

