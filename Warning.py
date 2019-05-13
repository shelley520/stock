#coding:utf-8
import ConfigParser
from Stock import Stock

class Warning():
    def __init__(self,stock_num,high,low):
        self.stock_num = stock_num
        self.high = high
        self.low = low

    def stock_message(self,stock_price):
        result = 0
        if self.low < stock_price < self.high:
            return result
        else:
            if stock_price > self.high:
                message = "股票：{},现价大于{},可以卖出".format(self.stock_num,self.high)
            elif stock_price < self.low:
                message = "股票：{},现价低于{},可以买入".format(self.stock_num,self.low)
            return message
